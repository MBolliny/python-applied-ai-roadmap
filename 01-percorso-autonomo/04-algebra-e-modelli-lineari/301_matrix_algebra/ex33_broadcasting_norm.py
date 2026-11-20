import numpy as np

# 1. Setup dati: 8 canali su 100.000 campioni
# Ogni canale ha media diversa (~10, ~20, ...) e scala diversa
offset = np.array([10, 20, 30, 40, 50, 60, 70, 80]).reshape(8, 1)
telemetria = np.random.normal(loc=0.0, scale=2.0, size=(8, 100_000)) + offset

# 2. Calcolo media e deviazione standard mantenendo la dimensione 2D (8, 1)
# keepdims=True fa sì che la forma sia (8, 1) invece di (8,)
mu = np.mean(telemetria, axis=1, keepdims=True)
sigma = np.std(telemetria, axis=1, keepdims=True)

print(f"Shape telemetria originaria: {telemetria.shape}")
print(f"Shape mu (con keepdims):     {mu.shape}")
print(f"Shape sigma (con keepdims):  {sigma.shape}")
print("-" * 50)

# 3. Normalizzazione via Broadcasting: (8, 100_000) - (8, 1) / (8, 1)
telemetria_norm = (telemetria - mu) / sigma

# 4. Verifica matematica: su tutti gli 8 canali mu deve essere ~0 e sigma ~1
mu_post = np.mean(telemetria_norm, axis=1)
sigma_post = np.std(telemetria_norm, axis=1)

print(f"Medie post-normalizzazione (devono essere ~0.0):\n{np.round(mu_post, 3)}")
print(f"Deviazioni post-normalizzazione (devono essere ~1.0):\n{np.round(sigma_post, 3)}")
