import funzioni_input
from pathlib import Path

CARTELLA_LAVORO: Path = Path(__file__).resolve().parent.parent
CARTELLA_DATI: Path = CARTELLA_LAVORO / "dati"

if __name__ == "__main__":

    # preparazione dell'ambiente creando la cartella di accumolo dati
    file_sessione = funzioni_input.crea_nuovo_percorso(CARTELLA_DATI)
    soglia_sessione_lunga = 30

    # inserimento dati da input
    funzioni_input.carica_dati_JSON(file_sessione, funzioni_input.raccogli_input())
