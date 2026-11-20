"""Modulo pipeline per l'elaborazione dei log dell'incubatrice biologica.

Flusso dati:
    File CSV -> parse_line() -> data_validation() -> update_session_data() -> export_session_reports()
"""

import json
from pathlib import Path
from pprint import pprint


def file_data_reading(file_path: Path) -> dict[str, dict]:
    """Legge il CSV grezzo riga per riga, filtra le letture anomale e aggrega i dati.

    Args:
        file_path: Percorso del file CSV di input.

    Returns:
        dict[str, dict]: Dizionario allocato sull'heap contenente le metriche parziali
        raggruppate per session_id (es. 'RUN-A').
    """
    # Struttura principale: viene creata qui e popolata 'in-place' tramite riferimento
    session_data: dict[str, dict] = {}

    with file_path.open(mode="r", encoding="utf-8") as file_index:
        for line in file_index:
            # 1. Parsing: estrae la tupla tipizzata (session_id, timestamp, temp, ph)
            parsed_data = parse_line(line)

            # 2. Validazione biologica: scarta i campioni fuori range
            if data_validation(parsed_data):
                print("dato " + str(parsed_data) + " valido")
                # Nota: session_data è passato per riferimento, la funzione modifica il dict originale
                update_session_data(
                    session_data,
                    parsed_data[0],  # session_id
                    parsed_data[2],  # temp_celsius
                    parsed_data[3],  # ph
                )
            else:
                print("Dato " + str(parsed_data) + " non valido")
                continue

    return session_data


def parse_line(data_line: str) -> tuple[str, int, float, float]:
    """Esegue la pulizia e il casting dei tipi per una singola riga CSV.

    Formato atteso: "session_id,timestamp,temp_celsius,ph"
    Mappa indici restituita:
        [0]: session_id (str)
        [1]: timestamp (int, epoca UNIX)
        [2]: temp_celsius (float)
        [3]: ph (float)
    """
    # Rimozione spazi/newline e split sui separatori
    cleaned_line = data_line.strip().split(",")

    session_id = cleaned_line[0]
    timestamp = int(cleaned_line[1])
    temp_celsius = float(cleaned_line[2])
    ph = float(cleaned_line[3])

    return session_id, timestamp, temp_celsius, ph


def data_validation(parsed_data: tuple | list) -> bool:
    """Verifica che i parametri fisici/chimici rispettino i limiti biologici vitali.

    Range ammessi per l'incubatrice:
        - Temperatura: [30.0, 42.0] °C
        - pH:          [6.5, 8.0]
    """
    min_temp: float = 30.0
    max_temp: float = 42.0
    min_ph: float = 6.5
    max_ph: float = 8.0

    temp_celsius = parsed_data[2]
    ph = parsed_data[3]

    # Controllo a intervallo chiuso (entrambi gli estremi sono inclusi)
    if not (min_temp <= temp_celsius <= max_temp) or not (min_ph <= ph <= max_ph):
        return False

    return True


def update_session_data(
    sessions: dict[str, dict], session_id: str, temp: float, ph: float
) -> None:
    """Aggiorna le metriche cumulative della sessione modificando il dizionario sul posto.

    Attenzione:
        - Non restituisce nulla (-> None). L'oggetto 'sessions' viene mutato direttamente in RAM.
        - Per la temperatura usa la formula della media mobile progressiva:
            nuova_media = (vecchia_media * vecchi_campioni + nuova_temp) / nuovi_campioni
        - Per il pH memorizza l'ultimo valore valido registrato.
    """
    if session_id not in sessions:
        # Primo campione valido per questo session_id: inizializza estremi e medie
        sessions[session_id] = {
            "valid_sample": 1,
            "max_temp_celsius": temp,
            "min_temp_celsius": temp,
            "avg_temp_celsius": temp,
            "ph": ph,
        }
    else:
        # Aggiornamento record esistente
        entry = sessions[session_id]
        entry["valid_sample"] += 1
        entry["max_temp_celsius"] = max(entry["max_temp_celsius"], temp)
        entry["min_temp_celsius"] = min(entry["min_temp_celsius"], temp)

        # Ricalcolo media senza tenere in memoria la lista completa di tutti i valori passati
        prev_count = entry["valid_sample"] - 1
        entry["avg_temp_celsius"] = (
            entry["avg_temp_celsius"] * prev_count + temp
        ) / entry["valid_sample"]
        entry["ph"] = ph


def export_session_reports(sessions: dict[str, dict], output_path: Path) -> None:
    """Arrotonda i risultati finali, assegna lo stato e salva il report in formato JSON.

    - Arrotonda tutte le grandezze floating-point a 2 cifre decimali.
    - Crea in automatico le cartelle genitore se non esistono (evita FileNotFoundError).
    """
    consolidated_report: dict[str, dict] = {}

    for session_id, metrics in sessions.items():
        consolidated_report[session_id] = {
            "status": "COMPLETED",
            "samples_count": metrics["valid_sample"],
            "temp_min_celsius": round(metrics["min_temp_celsius"], 2),
            "temp_max_celsius": round(metrics["max_temp_celsius"], 2),
            "temp_avg_celsius": round(metrics["avg_temp_celsius"], 2),
            "ph_avg": round(metrics["ph"], 2),
        }

    # Assicura l'esistenza della cartella (es. 'output/') prima di aprire il file in scrittura
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open(mode="w", encoding="utf-8") as json_file:
        json.dump(consolidated_report, json_file, indent=4)