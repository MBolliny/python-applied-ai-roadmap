"""
PIPELINE DI PREDICTIVE MAINTENANCE: CLASSIFICAZIONE BINARIA FROM-SCRATCH
Dominio: Rilevamento guasti imminenti su telemetria industriale a 4 canali.
Architettura: Modello Lineare + Attivazione Sigmoide (Regressione Logistica).
Ottimizzazione: Gradient Descent su Binary Cross-Entropy con clipping numerico.
"""

import numpy as np

# Per garantire la riproducibilità numerica esatta su ogni macchina
np.random.seed(42)


# ==============================================================================
# FASE 0: GENERAZIONE DELLA TELEMETRIA SINTETICA
# Simulazione fisica di 2500 campioni temporali (4 canali sensore continui).
# ==============================================================================

n_samples = 2500

# 1. Canale 0: Temperatura (°C) - Distribuzione gaussiana attorno a regime nominale
temp = np.random.normal(loc=70.0, scale=8.0, size=(n_samples, 1))

# 2. Canale 1: Vibrazione (mm/s) - Misura del gioco meccanico sui cuscinetti
vib = np.random.normal(loc=2.5, scale=1.2, size=(n_samples, 1))

# 3. Canale 2: Velocità di rotazione (RPM)
rpm = np.random.normal(loc=3000.0, scale=150.0, size=(n_samples, 1))

# 4. Canale 3: Pressione circuito olio lubrificante (bar)
oil_press = np.random.normal(loc=4.5, scale=0.6, size=(n_samples, 1))

# Matrice delle feature grezze: dimensione (2500, 4)
X_raw = np.hstack([temp, vib, rpm, oil_press])

# Meccanismo causale a terra (Ground Truth):
# Il guasto è innescato principalmente da un'anomalia congiunta vibrazione/temperatura.
ground_truth_score = (
    0.3 * (temp - 70.0)
    + 2.5 * (vib - 2.5)
    - 0.8 * (oil_press - 4.5)
    + np.random.normal(0, 1.0, size=(n_samples, 1))
)

# Target binario: 1 = Guasto / Allarme, 0 = Nominale (soglia a zero sullo score latente)
y_raw = (ground_truth_score > 1.5).astype(float)


# ==============================================================================
# FASE 1: PREPARAZIONE DATI (SPLIT & DATA LEAKAGE PREVENTION)
# Divisione 80/20 e scaling Z-score calcolato ESCLUSIVAMENTE sul training set.
# ==============================================================================

# 1. Train / Test Split deterministico (2000 campioni train, 500 campioni test)
train_ratio = 0.8
n_train = int(n_samples * train_ratio)

# Shuffle congiunto degli indici per rompere correlazioni temporali artificiali
indices = np.random.permutation(n_samples)
train_idx, test_idx = indices[:n_train], indices[n_train:]

X_train, y_train = X_raw[train_idx], y_raw[train_idx]
X_test, y_test = X_raw[test_idx], y_raw[test_idx]

# 2. Standardizzazione Z-Score: (X - media) / deviazione_standard
# Cruciale: media e varianza si stimano SOLO sul train per non inquinare il test
mu = np.mean(X_train, axis=0)
sigma = np.std(X_train, axis=0)

# Prevenzione divisione per zero nel caso un sensore abbia varianza nulla
sigma = np.where(sigma == 0.0, 1.0, sigma)

X_train_scaled = (X_train - mu) / sigma
X_test_scaled = (X_test - mu) / sigma


# ==============================================================================
# FASE 2: DEFINIZIONE DEI MATTONI MATEMATICI DEL MODELLO
# ==============================================================================

def sigmoid(z):
    """
    Funzione di attivazione: proietta il punteggio continuo (-inf, +inf)
    nell'intervallo (0, 1) per interpretarlo come probabilità a posteriori.
    """
    return 1.0 / (1.0 + np.exp(-z))


def predict_proba(X, W, b):
    """
    Forward Pass vettoriale completo: Z = X @ W + b seguito da sigmoide.
    Ritorna la matrice delle probabilità stimate y_hat con forma (N, 1).
    """
    return sigmoid(X @ W + b)


def compute_loss(y_true, y_pred):
    """
    Binary Cross-Entropy (Log Loss).
    Misura la divergenza probabilistica tra previsioni continue e target reali.
    Applica il clipping per impedire overflow/underflow su log(0).
    """
    N = y_true.shape[0]
    eps = 1e-15
    y_pred_safe = np.clip(y_pred, eps, 1.0 - eps)

    # Media delle penalità individuali
    loss = - (1.0 / N) * np.sum(
        y_true * np.log(y_pred_safe) + (1.0 - y_true) * np.log(1.0 - y_pred_safe)
    )
    return loss


# ==============================================================================
# FASE 3: TRAINING LOOP (BATCH GRADIENT DESCENT)
# Discesa analitica lungo la superficie d'errore convessa della Loss.
# ==============================================================================

n_features = X_train_scaled.shape[1]
epochs = 1000
learning_rate = 0.1
N_train = X_train_scaled.shape[0]

# Inizializzazione neutra (pesi nulli, massima entropia iniziale: y_hat = 0.5)
W = np.zeros((n_features, 1))
b = 0.0

print(f"--- FASE 3: AVVIO ADDESTRAMENTO ({epochs} epoche, lr={learning_rate}) ---")

for epoch in range(1, epochs + 1):
    # 1. Forward Pass
    y_hat = predict_proba(X_train_scaled, W, b)

    # 2. Calcolo scarto vettoriale (Previsione - Verità)
    error = y_hat - y_train

    # 3. Proiezione dell'errore sui sensori (Gradiente analitico dW e db)
    dW = (1.0 / N_train) * (X_train_scaled.T @ error)
    db = (1.0 / N_train) * np.sum(error)

    # 4. Aggiornamento parametri nella direzione opposta alla salita dell'errore
    W = W - learning_rate * dW
    b = b - learning_rate * db

    # Monitoraggio periodico per verificare la discesa della curva
    if epoch % 200 == 0 or epoch == 1:
        current_loss = compute_loss(y_train, y_hat)
        print(f"Epoca {epoch:4d}/{epochs} | Loss di Training: {current_loss:.4f}")

print("--- TRAINING COMPLETATO ---\n")


# ==============================================================================
# FASE 4: AUDIT PARAMETRI E VALUTAZIONE SUL TEST SET
# Validazione della capacità di generalizzazione su dati mai visti.
# ==============================================================================

# 1. Ispezione dell'importanza fisica attribuita ai sensori
sensor_names = ["Temperatura", "Vibrazione", "RPM", "Pressione Olio"]
print("=== PARAMETRI FINALI DEL MODELLO ===")
for name, weight in zip(sensor_names, W.flatten()):
    print(f"Peso {name:<16}: {weight:+7.4f}")
print(f"Bias d'intercetta (b) : {b:+7.4f}\n")

# 2. Inferenza sul Test Set (dati non usati per l'aggiornamento dei pesi)
y_test_prob = predict_proba(X_test_scaled, W, b)
test_loss = compute_loss(y_test, y_test_prob)

# 3. Decisione operativa: conversione probabilità continua -> allarme binario (soglia 0.5)
threshold = 0.5
y_test_pred = (y_test_prob >= threshold).astype(float)

# 4. Metriche di prestazione e Matrice di Confusione
accuracy = np.mean(y_test_pred == y_test) * 100.0

tp = np.sum((y_test_pred == 1.0) & (y_test == 1.0))  # Veri Positivi (Guasti intercettati)
fp = np.sum((y_test_pred == 1.0) & (y_test == 0.0))  # Falsi Positivi (Falsi allarmi)
tn = np.sum((y_test_pred == 0.0) & (y_test == 0.0))  # Veri Negativi (Nominali corretti)
fn = np.sum((y_test_pred == 0.0) & (y_test == 1.0))  # Falsi Negativi (Guasti mancati - critico!)

print("=== VERIFICA DI GENERALIZZAZIONE (TEST SET: 500 CAMPIONI) ===")
print(f"Loss sul Test Set : {test_loss:.4f}")
print(f"Accuratezza Totale: {accuracy:.2f}%\n")

print("--- MATRICE DI CONFUSIONE OPERATIVA ---")
print(f"Guasti correttamente intercettati (TP): {tp:3d} | Falsi Allarmi      (FP): {fp:3d}")
print(f"Guasti mancati / silenti    (FN): {fn:3d} | Nominali corretti  (TN): {tn:3d}")
