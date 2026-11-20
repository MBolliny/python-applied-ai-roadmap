import numpy as np
from sklearn.datasets import make_classification
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score, KFold

# 1. Setup dati: 10.000 campioni, 20 feature
X, y = make_classification(
    n_samples=10_000,
    n_features=20,
    n_informative=5,
    random_state=42
)

cv = KFold(n_splits=5, shuffle=True, random_state=42)

# 2. Percorso A: Flusso INGENUO con Data Leakage
# Calcola mu e sigma sull'INTERA matrice X prima dello split
scaler_leak = StandardScaler()
X_leaked = scaler_leak.fit_transform(X)
clf_leak = LogisticRegression(solver='liblinear')
scores_leaked = cross_val_score(clf_leak, X_leaked, y, cv=cv)

# 3. Percorso B: Flusso BLINDATO con Scikit-Learn Pipeline
# Lo scaler calcola mu e sigma SOLO sul train fold a ogni iterazione
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('clf', LogisticRegression(solver='liblinear'))
])
scores_pipeline = cross_val_score(pipeline, X, y, cv=cv)

# 4. Confronto a video
print(f"Accuracy Flusso con Leakage (Ingenuo):  {np.mean(scores_leaked):.4f} (+/- {np.std(scores_leaked):.4f})")
print(f"Accuracy Flusso Blindato (Pipeline):    {np.mean(scores_pipeline):.4f} (+/- {np.std(scores_pipeline):.4f})")
print(f"Delta di accuratezza (Bias introdotto): {np.mean(scores_leaked) - np.mean(scores_pipeline):+.4f}")
