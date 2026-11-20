import numpy as np

# 1. Setup dati: 8 canali ECG registrati per 100.000 campioni temporali ciascuno
# Matrice di forma (8, 100_000)
telemetria = np.random.normal(loc=0.0, scale=1.5, size=(8, 100_000))

# 2. Estrazione metriche vettorizzata senza loop (axis=1 collassa il tempo)
medie = np.mean(telemetria, axis=1)
varianze = np.var(telemetria, axis=1)
picchi_assoluti = np.max(np.abs(telemetria), axis=1)

# 3. Output a video: verifichiamo che la forma risultante sia (8,) e non (100000,)
print(f"Shape matrice originaria: {telemetria.shape}")
print(f"Shape vettore medie:      {medie.shape}")
print(f"Shape vettore varianze:   {varianze.shape}")
print(f"Shape vettore picchi:     {picchi_assoluti.shape}")
print("-" * 50)
print(f"Valori medi per gli 8 canali:\n{medie}")
print(f"Picchi assoluti per gli 8 canali:\n{picchi_assoluti}")
