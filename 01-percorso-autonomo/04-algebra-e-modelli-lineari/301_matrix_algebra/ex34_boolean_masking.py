import numpy as np
import time

# 1. Setup dati identico allo Spike 3.4 (1 milione di float32)
np.random.seed(42)
segnale = np.random.laplace(loc=0.0, scale=1.2, size=1_000_000).astype(np.float32)
segnale[::10_000] = 12.5
segnale[1::10_000] = -12.5

# 2. Approccio A: Branching software classico (ciclo for + if/elif/else)
t0_if = time.perf_counter()
risultato_if = []
for x in segnale:
    if x > 5.0:
        risultato_if.append(5.0)
    elif x < -5.0:
        risultato_if.append(-5.0)
    else:
        risultato_if.append(float(x))
t1_if = time.perf_counter()
tempo_if_ms = (t1_if - t0_if) * 1000

# 3. Approccio B: Clamping vettoriale NumPy (ALU + MUX hardware)
t0_np = time.perf_counter()
risultato_np = np.clip(segnale, a_min=-5.0, a_max=5.0)
t1_np = time.perf_counter()
tempo_np_ms = (t1_np - t0_np) * 1000

# 4. Confronto e certificazione
accelerazione = tempo_if_ms / tempo_np_ms

print(f"=== BENCHMARK CLAMPING (N = {len(segnale):,}) ===")
print(f"Tempo Ciclo con IF/ELSE (Python): {tempo_if_ms:.3f} ms")
print(f"Tempo np.clip (Hardware/SIMD):    {tempo_np_ms:.3f} ms")
print(f"FATTORE DI ACCELERAZIONE:         {accelerazione:.1f}x più veloce")
