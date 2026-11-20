import numpy as np
import time

# 1. Setup dati: 5 milioni di campioni numerici contigui in RAM
N = 5_000_000
segnale = np.random.randn(N).astype(np.float32)

# 2. Approccio A: Ciclo for standard in Python (un elemento alla volta)
t0_for = time.perf_counter()
risultato_for = []
for x in segnale:
    risultato_for.append(abs(x) + 0.5 * (x ** 2))
t1_for = time.perf_counter()
tempo_for = t1_for - t0_for

# 3. Approccio B: Vettorizzazione pura con NumPy (motore SIMD su registri CPU)
t0_np = time.perf_counter()
risultato_np = np.abs(segnale) + 0.5 * (segnale ** 2)
t1_np = time.perf_counter()
tempo_np = t1_np - t0_np

# 4. Confronto prestazioni
accelerazione = tempo_for / tempo_np

print(f"=== BENCHMARK VETTORIZZAZIONE (N = {N:,}) ===")
print(f"Tempo Ciclo For (Python): {tempo_for:.4f} s")
print(f"Tempo Vettorizzato (NumPy): {tempo_np:.4f} s")
print(f"FATTORE DI ACCELERAZIONE:  {accelerazione:.1f}x più veloce")
