import funzioni_elaborazione
from pathlib import Path
import json

CARTELLA_LAVORO: Path = Path(__file__).resolve().parent.parent
CARTELLA_DATI: Path = CARTELLA_LAVORO / "dati"

if __name__ == "__main__":

    soglia_sessione_lunga = 30
    file_scelto = funzioni_elaborazione.seleziona_file_sessione(CARTELLA_DATI)

    if file_scelto is not None:
        lista_sessioni_studio = funzioni_elaborazione.leggi_dati_JSON(file_scelto)

    # celaborazione dati
    tempo_studiato, lista_sessioni_studio = funzioni_elaborazione.calcola_sessioni_studio(soglia_sessione_lunga, lista_sessioni_studio)
    funzioni_elaborazione.stampa_analisi(funzioni_elaborazione.calcola_ora(tempo_studiato), lista_sessioni_studio, soglia_sessione_lunga)


