# spostamento nella cartella per importazine
from pathlib import Path
import sys

percorso_test = Path(__file__).resolve()
cartella_progetto = percorso_test.parent.parent
cartella_sorgenti = cartella_progetto / "src"
sys.path.append(str(cartella_sorgenti))

from canale_vitale import CanaleVitale

# test LETTURA
canale_bpm = CanaleVitale("BPM", "bpm", [30.0, 220.0])

# test SCRITTURA
campioni_test = [72.0, 15.0, 85.5, 260.0, 64.0, "25,1"]
# campioni_test = []

for campione in campioni_test:

    try:
        canale_bpm.registra_campione(campione)

    except TypeError as err:
        print("errore di tipo su", {campione}, "raccolto")

    except ValueError as err:
        print("errore di valore su", {campione}, "raccolto")

# calcolo della statistica
print("max-media: ", {canale_bpm.calcola_statistiche()})

# verifica dei dunder
print("Lunghezza rilevata con len():", len(canale_bpm))


# dati finali
print("\n--- STATO FINALE DELLO STORICO ---")
# Verifichiamo che i valori scartati (15.0 e 260.0) non siano entrati nella lista
print(f"Campioni memorizzati: {canale_bpm.storico_dati}")
print(f"Numero campioni validi salvati: {len(canale_bpm.storico_dati)}")
