import time

numeri = list(range(1_000_000))
lista = numeri
insieme = set(numeri)

inizio = time.perf_counter()
for _ in range(100):
    999_999 in lista
print("lista:", time.perf_counter() - inizio, "secondi")

inizio = time.perf_counter()
for _ in range(100):
    999_999 in insieme
print("insieme:", time.perf_counter() - inizio, "secondi")
