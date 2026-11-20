import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold, GroupKFold, cross_val_score

# 1. Setup realistico: 50 pazienti, 20 finestre temporali ciascuno = 1.000 campioni totali
np.random.seed(42)
n_pazienti = 50
finestre_per_paziente = 20
n_campioni = n_pazienti * finestre_per_paziente
groups = np.repeat(np.arange(n_pazienti), finestre_per_paziente)

# Ogni paziente ha una diagnosi reale assegnata (metà sani = 0, metà patologici = 1)
diagnosi_per_paziente = np.random.randint(0, 2, size=n_pazienti)
y = diagnosi_per_paziente[groups]

# L'impronta anatomica del paziente domina il segnale (rumore specifico per soggetto)
impronta_paziente = np.random.randn(n_pazienti, 20) * 2.5
rumore_sensore = np.random.randn(n_campioni, 20) * 0.8

# Matrice X: le feature riflettono primariamente il corpo del paziente
X = impronta_paziente[groups] + rumore_sensore

# 2. Modello decisionale ad albero
clf = RandomForestClassifier(n_estimators=50, random_state=42)

# 3. Percorso A: KFold Ingenuo (mescola finestre dello stesso paziente tra train e test)
cv_ingenuo = KFold(n_splits=5, shuffle=True, random_state=42)
scores_ingenuo = cross_val_score(clf, X, y, cv=cv_ingenuo)

# 4. Percorso B: GroupKFold Rigoroso (isola interi pazienti tra train e test)
cv_gruppi = GroupKFold(n_splits=5)
scores_gruppi = cross_val_score(clf, X, y, cv=cv_gruppi, groups=groups)

# 5. Output di verifica clinica
media_ingenuo = np.mean(scores_ingenuo) * 100
media_gruppi = np.mean(scores_gruppi) * 100
delta = media_ingenuo - media_gruppi

print(f"Valutazione Ingenua (KFold):              Accuracy = {media_ingenuo:.1f}%  (Illusione clinica)")
print(f"Valutazione Paziente-Cieco (GroupKFold):  Accuracy = {media_gruppi:.1f}%  (Performance reale)")
print(f"DELTA REALE (Crollo su nuovi pazienti):    -{delta:.1f}%")
