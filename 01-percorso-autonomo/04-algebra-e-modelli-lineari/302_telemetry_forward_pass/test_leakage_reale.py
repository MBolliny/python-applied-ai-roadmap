import numpy as np
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# 1. Creiamo 100 pazienti e 1.000 parametri di PURO RUMORE CASUALE (monete truccate)
np.random.seed(42)
X = np.random.randn(100, 1000)      # Rumore puro
y = np.random.randint(0, 2, size=100) # Diagnosi a caso (0 o 1)

# ==========================================
# FLUSSO A: LA TRUFFA (Data Leakage)
# Seleziono le 5 "migliori" feature guardando TUTTI i 100 pazienti PRIMA di dividere
# ==========================================
selettore_truffa = SelectKBest(f_classif, k=5)
X_selezionato = selettore_truffa.fit_transform(X, y)

X_train, X_test, y_train, y_test = train_test_split(X_selezionato, y, test_size=0.3, random_state=42)
modello_truffa = LogisticRegression()
modello_truffa.fit(X_train, y_train)
score_truffa = modello_truffa.score(X_test, y_test)

# ==========================================
# FLUSSO B: IL METODO RIGOROSO (Blindato)
# Divido PRIMA. Seleziono le 5 feature SOLO sui 70 pazienti di train!
# ==========================================
X_train_raw, X_test_raw, y_train_raw, y_test_raw = train_test_split(X, y, test_size=0.3, random_state=42)

selettore_onesto = SelectKBest(f_classif, k=5)
X_train_onesto = selettore_onesto.fit_transform(X_train_raw, y_train_raw)
# Il test set subisce la scelta fatta dal train, non viene consultato!
X_test_onesto = selettore_onesto.transform(X_test_raw)

modello_onesto = LogisticRegression()
modello_onesto.fit(X_train_onesto, y_train_raw)
score_onesto = modello_onesto.score(X_test_onesto, y_test_raw)

print(f"Accuracy con Truffa (Data Leakage): {score_truffa * 100:.1f}%  <-- Sembra un miracolo!")
print(f"Accuracy Onesta (Reale sul rumore): {score_onesto * 100:.1f}%  <-- La realtà (testa o croce)")
