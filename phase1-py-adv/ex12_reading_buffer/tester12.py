# Import puntato al tuo file di lavoro:
from ex12_reading_buffer import ReadingBuffer

# Per verificare a specchio la soluzione, basta scambiare l'import:
# from ex12_reading_buffer_sol import ReadingBuffer

print("--- AVVIO VERIFICA LINEARE EX12 ---")

# TEST 1: Protocollo len(), str() e repr()
buffer_ecg = ReadingBuffer("ECG_LEAD_I", [1.0, 1.2])
buffer_ecg.add_reading(1.5)

# Verifica conteggio len()
lunghezza = len(buffer_ecg)
if lunghezza == 3:
    print(f"[OK] len(buffer) corretto: {lunghezza}")
else:
    print(f"[FAIL] len(buffer) errato: atteso 3, ottenuto {lunghezza}")

# Verifica formattazione str()
testo_operatore = str(buffer_ecg)
if testo_operatore == "Sensor ECG_LEAD_I: 3 readings":
    print(f"[OK] str(buffer) corretto: {testo_operatore}")
else:
    print(f"[FAIL] str(buffer) errato: {testo_operatore}")

# Verifica rappresentazione repr()
testo_debug = repr(buffer_ecg)
atteso_repr = "ReadingBuffer(sensor_name='ECG_LEAD_I', readings=[1.0, 1.2, 1.5])"
if testo_debug == atteso_repr:
    print(f"[OK] repr(buffer) corretto: {testo_debug}")
else:
    print(f"[FAIL] repr(buffer) errato: {testo_debug}")

# TEST 2: Protocollo di uguaglianza __eq__ (==)
b1 = ReadingBuffer("S1", [10.0, 20.0])
b2 = ReadingBuffer("S1", [10.0, 20.0])
b3 = ReadingBuffer("S2", [10.0])

# Confronto tra buffer uguali
if b1 == b2:
    print("[OK] b1 == b2 rilevato correttamente (True)")
else:
    print("[FAIL] b1 == b2 fallito: dovrebbero essere uguali")

# Confronto tra buffer diversi per canale e dati
if not (b1 == b3):
    print("[OK] b1 == b3 rilevato correttamente come diverso (False)")
else:
    print("[FAIL] b1 == b3 fallito: dovrebbero essere diversi")

# Confronto con un tipo completamente estraneo
if not (b1 == "non_un_buffer"):
    print("[OK] Confronto con tipo estraneo gestito correttamente (False)")
else:
    print("[FAIL] Confronto con stringa ha prodotto True invece di False")