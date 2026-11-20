# ==============================================================================
# EXERCISE 01: INDUSTRIAL PUMP CAVITATION PREDICTION (BINARY LOGISTIC REGRESSION)
# ==============================================================================

import numpy as np


# 1. Feature matrix X: Shape (N=3 samples, D=2 sensors)
# Column 0: Standardized Hydraulic Pressure (x1)
# Column 1: Standardized Pump Housing Vibration (x2)
X_train = np.array([
    [ 1.0,  2.0],
    [-1.0, -1.0],
    [ 0.0,  1.0]
], dtype=np.float64)

# 2. Ground truth target vector y: Shape (N=3, 1)
# 1 = Cavitation / Failure, 0 = Nominal Operation
y_sol = np.array([
    [1.0],
    [0.0],
    [1.0]
], dtype=np.float64)

# 3. Model parameters: Weights vector W of shape (D=2, 1) and scalar bias b
W = np.array([
    [0.5],
    [1.0]
], dtype=np.float64)

b = -0.5

# calcolo output
Z = X_train @ W + b
y_hat = 1.0 / (1.0 + np.exp(-Z))
print(f"output normalizzato: \n{y_hat}")

# verifica dell'errore
error = y_sol - y_hat

# calcolo dei nuovi pesi
alpha = 0.1
N = X_train.shape[0]

dW = (1.0 / N) * (X_train.T @ error)
db = (1.0 / N) * np.sum(error)

W = W - alpha * dW
b = b - alpha * db

# visualizzazione risultati
print("Previsioni y_hat:\n", y_hat)
print("\nErrore residuo:\n", error)
print("\nGradienti calcolati:")
print("dW:\n", dW)
print("db:", db)
print("\nParametri aggiornati:")
print("W nuovo:\n", W)
print("b nuovo:", b)
