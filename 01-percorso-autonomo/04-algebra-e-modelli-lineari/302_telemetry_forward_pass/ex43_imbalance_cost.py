import numpy as np
import time
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import confusion_matrix, classification_report

# 1. Setup dati: 5.000 pazienti, sbilanciamento clinico estremo (98% Sani, 2% Critici)
X, y = make_classification(
    n_samples=5_000,
    n_features=15,
    n_informative=5,
    weights=[0.98, 0.02],
    random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"Campioni Test totali: {len(y_test)} (Sani: {np.sum(y_test == 0)}, Critici: {np.sum(y_test == 1)})\n")

# ==========================================
# TEST 1: Modello Standard (Ingenuo, non bilanciato)
# ==========================================
t0 = time.perf_counter()
clf_standard = HistGradientBoostingClassifier(random_state=42)
clf_standard.fit(X_train, y_train)
preds_std = clf_standard.predict(X_test)
t_std_ms = (time.perf_counter() - t0) * 1000

cm_std = confusion_matrix(y_test, preds_std)

# ==========================================
# TEST 2: Modello Clinico (class_weight='balanced')
# ==========================================
t0 = time.perf_counter()
clf_balanced = HistGradientBoostingClassifier(class_weight='balanced', random_state=42)
clf_balanced.fit(X_train, y_train)
preds_bal = clf_balanced.predict(X_test)
t_bal_ms = (time.perf_counter() - t0) * 1000

cm_bal = confusion_matrix(y_test, preds_bal)

# Output diagnostico e prestazioni hardware
print(f"--- 1. MODELLO STANDARD (Tempo training+inference: {t_std_ms:.2f} ms) ---")
print(f"Accuratezza ingannevole: {(preds_std == y_test).mean() * 100:.1f}%")
print(f"Pazienti critici PERSI (Falsi Negativi): {cm_std[1, 0]} su {np.sum(y_test == 1)}")

print(f"\n--- 2. MODELLO BILANCIATO (Tempo training+inference: {t_bal_ms:.2f} ms) ---")
print(f"Accuratezza reale:       {(preds_bal == y_test).mean() * 100:.1f}%")
print(f"Pazienti critici PERSI (Falsi Negativi): {cm_bal[1, 0]} su {np.sum(y_test == 1)}")

print("\n--- MATRICE DI CONFUSIONE DEL MODELLO BILANCIATO ---")
print(f"Sani confermati (TN): {cm_bal[0, 0]}  |  Falsi Allarmi (FP): {cm_bal[0, 1]}")
print(f"Malati persi    (FN): {cm_bal[1, 0]}  |  Vite Salvate  (TP): {cm_bal[1, 1]}")

# Estraiamo la probabilità continua anziché il responso secco 0/1
probabilita_malato = clf_balanced.predict_proba(X_test)[:, 1]

# Abbassiamo la soglia clinica di allarme: basta il 20% di probabilità per far scattare il campanello
preds_soglia_clinica = (probabilita_malato >= 0.20).astype(int)
cm_soglia = confusion_matrix(y_test, preds_soglia_clinica)

print("\n--- 3. MODELLO BILANCIATO CON SOGLIA CLINICA (p >= 0.20) ---")
print(f"Pazienti critici PERSI (Falsi Negativi): {cm_soglia[1, 0]} su {np.sum(y_test == 1)}")
print(f"Vite Salvate           (Veri Positivi):  {cm_soglia[1, 1]} su {np.sum(y_test == 1)}")
print(f"Falsi Allarmi          (Falsi Positivi): {cm_soglia[0, 1]} su {np.sum(y_test == 0)}")
