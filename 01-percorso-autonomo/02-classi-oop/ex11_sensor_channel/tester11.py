from ex11_sensor_channel_sol import CanaleSensore
from ex11_sensor_channel import channelSensor

print("--- AVVIO TEST CANALE SENSORE ---")

# 1. Creazione nominale (valore positivo)
sonda = channelSensor("PT100_01", 36.5)
print(f"[OK] Sonda creata: {sonda.identificativo} con valore {sonda.valore}")

# 2. Aggiornamento valido
sonda.imposta_valore(37.2)
print(f"[OK] Valore aggiornato a: {sonda.valore}")

# 3. Tentativo di inserire un valore negativo a runtime
try:
    sonda.imposta_valore(-5.0)
    print("[FAIL] Ha accettato un numero negativo!")
except ValueError as errore:
    print(f"[OK] Errore intercettato: {errore}")
    print(f"[OK] Il valore in memoria non è cambiato ed è ancora: {sonda.valore}")

# 4. Tentativo di creare una sonda già con valore negativo
try:
    sonda_difettosa = CanaleSensore("PRESS_01", -1.0)
    print("[FAIL] Ha creato la sonda con valore iniziale negativo!")
except ValueError as errore:
    print(f"[OK] Errore alla creazione intercettato: {errore}")
