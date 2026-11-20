import random
import time
import sys

# 1. Generazione dati sparsi (ID fino a 1.000.000)
telemetria_lista = [random.randint(1, 1_000_000) for _ in range(100_000)]
allarmi_lista = [random.randint(1, 1_000_000) for _ in range(1_000)]
telemetria_set = set(telemetria_lista)

# 2. Benchmark Lista
count_lista = 0
t0_lista = time.perf_counter()
for allarme in allarmi_lista:
    if allarme in telemetria_lista:
        count_lista += 1
t1_lista = time.perf_counter()
tempo_lista = t1_lista - t0_lista

# 3. Benchmark Set
count_set = 0
t0_set = time.perf_counter()
for allarme in allarmi_lista:
    if allarme in telemetria_set:
        count_set += 1
t1_set = time.perf_counter()
tempo_set = t1_set - t0_set

# 4. Memoria e Stampa
mem_lista = sys.getsizeof(telemetria_lista)
mem_set = sys.getsizeof(telemetria_set)

print(f"Dimensione Lista: {mem_lista:,} bytes")
print(f"Dimensione Set:   {mem_set:,} bytes")
print(f"Tempo Lista: {tempo_lista:.6f} s | Match: {count_lista}")
print(f"Tempo Set:   {tempo_set:.6f} s | Match: {count_set}")
print(f"Fattore di accelerazione: {tempo_lista / tempo_set:.1f}x")
