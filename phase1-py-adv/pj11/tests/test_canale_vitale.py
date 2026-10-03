# spostamento nella cartella per importazine
from pathlib import Path
import sys

percorso_test = Path(__file__).resolve()
cartella_progetto = percorso_test.parent.parent
cartella_sorgenti = cartella_progetto / "src"
sys.path.append(str(cartella_sorgenti))

from canale_vitale import CanaleVitale

# test LETTURA
canale_bpm = CanaleVitale("BPM", "bpm", 30.0, 220.0)

# verifica dello stato interno appena nato
print("--- VERIFICA INIZIALIZZAZIONE CANALE ---")
print("Identificativo:", canale_bpm.identificativo)
print("Unita di misura:", canale_bpm.misura)
print("Limite minimo:", canale_bpm.valore_minimo)
print("Limite massimo:", canale_bpm.valore_massimo)
print("Storico dati iniziale:", canale_bpm.storico_dati)

# test SCRITTURA
campioni_test = [72.0, 15.0, 85.5, 260.0, 64.0]

for campione in campioni_test:
    canale_bpm.registra_campione(campione)

print("\n--- STATO FINALE DELLO STORICO ---")
# Verifichiamo che i valori scartati (15.0 e 260.0) non siano entrati nella lista
print(f"Campioni memorizzati: {canale_bpm.storico_dati}")
print(f"Numero campioni validi salvati: {len(canale_bpm.storico_dati)}")
