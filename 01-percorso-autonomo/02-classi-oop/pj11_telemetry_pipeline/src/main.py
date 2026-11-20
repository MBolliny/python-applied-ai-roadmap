from pathlib import Path
import sys

# Risoluzione del percorso assoluto del file corrente
file_corrente = Path(__file__).resolve()
cartella_progetto = file_corrente.parent.parent
sys.path.append(str(cartella_progetto))

from canale_vitale import CanaleVitale
from data.raw_data import genera_flusso_telemetria_simulato
from paziente import Paziente

# ----- SETUP di lavoro -----
# dataset su cui lavorare
raw_data = genera_flusso_telemetria_simulato()

# preparazione base paziente-canali
paziente_rossi = Paziente("PAZ-001")

canale_bpm = CanaleVitale("BPM", "bpm", (30.0, 220.0))
canale_spo2 = CanaleVitale("SPO2", "%", (70.0, 100.0))
canale_pressione = CanaleVitale("PA_SISTOLICA", "mmHg", (50.0, 250.0))

canali_verificati = [canale_bpm, canale_spo2, canale_pressione]

# collegamento e inserimento paziente-canali
for canale in canali_verificati:
    paziente_rossi.collega_canale(canale)


# ----- passaggio ed elaborazione DATI -----
for identificativo, valore in raw_data:

    if identificativo not in paziente_rossi.canali:
        continue

    canale_selezionato = paziente_rossi.canali[identificativo]

    try:
        canale_selezionato.registra_campione(valore)

    except TypeError as err:
        print("errore di tipo su", {valore}, "raccolto")

    except ValueError as err:
        print("errore di valore su", {valore}, "raccolto")

# ----- statistica finale -----
for canale in canali_verificati:
   massimo, media = canale.calcola_statistiche()
   print(f"Canale: {canale.identificativo} | Max: {massimo} | Media: {media:.1f}")
