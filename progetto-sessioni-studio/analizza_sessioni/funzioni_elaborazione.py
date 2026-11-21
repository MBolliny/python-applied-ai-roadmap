import json

def leggi_dati_JSON(file_sessione: Path) -> list:
    """estrai lista da file JSON"""

    with file_sessione.open("r", encoding="utf-8") as file:
        return json.load(file)

def calcola_sessioni_studio(soglia: int, sessioni_studio: list) -> (int, int):
    """calcola quanto tempo (in minuti) abbiamo studiato e il numero disessioni lunghe oltre la soglia"""

    # inizilizzazione
    sum = 0
    count_sessione_lunghe = 0

    # somma lunghezza sessioni e verifica siano oltre la soglia
    for durata_sessione in sessioni_studio:
        sum += durata_sessione
        if durata_sessione > soglia:
            count_sessione_lunghe += 1

    return sum, count_sessione_lunghe

def calcola_ora(minuti_ingresso: int) -> tuple[int, int]:
    """Converte orario da minuti in formaot (ore,minuti)"""

    ore = 0

    # Incrementa le ore finché non si supera il totale dei minuti
    while minuti_ingresso - (60 * ore) >= 0:
        ore += 1

    # Sottrae 1 a 'ore' perché l'ultimo ciclo ha superato la soglia
    minuti_rimanenti = minuti_ingresso - (60 * (ore - 1))
    return ore - 1, minuti_rimanenti

def stampa_analisi(tempo_studiato: tuple[int, int], sessioni_studio: int, soglia_sessione_lunga: int) -> None:
    """Stampa a schermo il riepilogo del tempo totale studaito e il numero delle sessioni lunghe fatte"""

    print(
        f"Hai studiato un totale di {tempo_studiato[0]}h {tempo_studiato[1]}min"
        f" con {sessioni_studio} sessioni sopra i {soglia_sessione_lunga}"
        " minuti."
    )

def seleziona_file_sessione(cartella_dati: Path) -> Path | None:
    """  Mostra i file JSON presenti nella cartella numerati da 0 a N-1
    e permette all'utente di selezionarne uno tramite indice da terminale.
    """
    # Recupera e ordina tutti i file .json nella cartella
    lista_file: list[Path] = sorted(cartella_dati.glob("*.json"))

    if not lista_file:
        print("Nessun file di sessione trovato nella cartella.")
        return None

    # Stampa l'elenco numerato da 0 a N-1
    print("\n--- Sessioni disponibili ---")
    for indice, file in enumerate(lista_file):
        print(f"[{indice}] {file.name}")

    # Ciclo di validazione dell'input
    while True:
        scelta = input("\nInserisci il numero del file da analizzare: ").strip()

        if scelta.isdigit():
            indice_scelto = int(scelta)
            # Verifica che l'indice rientri nel range della lista
            if 0 <= indice_scelto < len(lista_file):
                return lista_file[indice_scelto]

        print(f"Scelta non valida. Inserisci un numero tra 0 e {len(lista_file) - 1}.")
