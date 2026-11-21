import json
from datetime import datetime

def raccogli_input() -> list:
    """prende da terminale i valori e li inserisce in una lista"""

    # inizializzazione
    TERMINATORE = "quit"
    lista_sessioni_studio: list = []

    # scorro fino a che esco avendo trovato il terminatore
    while True:
        valore = input("Minuti studiati ('quit' per uscire): ").strip().lower()

        if valore == TERMINATORE:
            break

        # se ho temrinatore il progreamma termina prima e non arriva a questa riga
        lista_sessioni_studio.append(int(valore))

    return lista_sessioni_studio

def carica_dati_JSON(file_sessione: Path, lista_input = list) -> None:
    """carica lista su file JSON"""

    # Evita di creare file vuoti se esci subito con 'quit'
    if not lista_input:
        return

    with file_sessione.open("w", encoding="utf-8") as file:
        json.dump(lista_input, file, indent=4)

def crea_nuovo_percorso(cartella: Path) -> Path:
    """crea nuovo file di lavoro formato JSON"""

    # 1. Crea la cartella 'dati' se non esiste ancora
    cartella.mkdir(parents=True, exist_ok=True)

    # 2. Genera un timestamp univoco (Anno-Mese-Giorno_Ore-Minuti-Secondi)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # 3. Restituisce il percorso del nuovo file JSON
    print(f"sessione_{timestamp}.json e' stato creato")
    return cartella / f"sessione_{timestamp}.json"
