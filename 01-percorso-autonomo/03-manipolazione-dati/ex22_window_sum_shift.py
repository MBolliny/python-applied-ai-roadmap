import collections
import random
import time

# 1. Setup stream simulato (frequenza cardiaca: ~70 bpm medi con picchi casuali)
N_CAMPIONI = 100_000
FINESTRA_W = 1_000

stream_dati = [random.randint(60, 90) for _ in range(N_CAMPIONI)]
# Inseriamo un'anomalia arbitraria al campione 50.000
stream_dati[50_000] = 160


# --- APPROCCIO A: NAIVE (Ricalcolo continuo con sum) -> O(N * W) ---
t0_naive = time.perf_counter()

anomalie_naive = 0
for i in range(FINESTRA_W, N_CAMPIONI):
    blocco = stream_dati[i - FINESTRA_W : i]  # slicing: O(W)
    media = sum(blocco) / FINESTRA_W          # sommatoria da capo: O(W)
    if stream_dati[i] > media + 30:
        anomalie_naive += 1

t1_naive = time.perf_counter()
tempo_naive = t1_naive - t0_naive


# --- APPROCCIO B: SLIDING WINDOW O(1) con collections.deque ---
t0_opt = time.perf_counter()

anomalie_opt = 0
buffer = collections.deque(stream_dati[:FINESTRA_W], maxlen=FINESTRA_W)
somma_corrente = sum(buffer)  # Unica sommatoria iniziale una tantum

for i in range(FINESTRA_W, N_CAMPIONI):
    nuovo_valore = stream_dati[i]
    valore_uscito = buffer[0]  # Elemento più vecchio che sta per uscire (O(1))

    # Aggiornamento algebrico O(1)
    somma_corrente = somma_corrente - valore_uscito + nuovo_valore
    buffer.append(nuovo_valore)  # Inserisce nuovo ed elimina il vecchio a O(1)

    media = somma_corrente / FINESTRA_W
    if nuovo_valore > media + 30:
        anomalie_opt += 1

t1_opt = time.perf_counter()
tempo_opt = t1_opt - t0_opt


# --- AUDIT PRESTAZIONALE ---
print(f"=== STREAM MONITORING: {N_CAMPIONI:,} campioni | Finestra W = {FINESTRA_W:,} ===")
print(f"Approccio Naive (sum su slice):   {tempo_naive:.4f} s | Anomalie: {anomalie_naive}")
print(f"Approccio O(1) (Sliding Window):   {tempo_opt:.4f} s | Anomalie: {anomalie_opt}")
print(f"FATTORE DI ACCELERAZIONE:          {tempo_naive / tempo_opt:.1f}x più veloce")
