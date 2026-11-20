import numpy as np
import time
from sklearn.ensemble import RandomForestClassifier
import shap

# 1. Costruiamo 5 biomarcatori con significato fisiologico chiaro
np.random.seed(42)
n_pazienti = 2_000

eta = np.random.uniform(20, 85, size=n_pazienti)                     # Anni
battito = np.random.normal(75, 15, size=n_pazienti)                  # bpm
spo2 = np.random.normal(97, 3, size=n_pazienti)                      # % ossigeno
pressione_sistolica = np.random.normal(120, 20, size=n_pazienti)     # mmHg
temperatura = np.random.normal(36.8, 0.7, size=n_pazienti)           # °C

feature_names = ["Età", "Frequenza_Cardiaca", "SpO2_Ossigeno", "Pressione_Sistolica", "Temperatura"]
X = np.column_stack([eta, battito, spo2, pressione_sistolica, temperatura])

# Regola fisiologica per generare la crisi clinica:
# Rischio alto se: SpO2 scende sotto 90% E battito sopra 110 bpm, oppure età avanzata con pressione estrema
rischio_clinico = (
    (spo2 < 90) * 3.0 +
    (battito > 110) * 2.5 +
    (pressione_sistolica > 160) * 1.5 +
    (eta > 75) * 1.0
)
y = (rischio_clinico > 3.0).astype(int)

# 2. Addestriamo una Random Forest
t0 = time.perf_counter()
model = RandomForestClassifier(n_estimators=60, random_state=42)
model.fit(X, y)
t_train_ms = (time.perf_counter() - t0) * 1000

# 3. Selezioniamo un paziente critico specifico (es. Mario Rossi con parametri anomali)
# Paziente: 78 anni, tachicardico (125 bpm), ipossico (SpO2 88%), pressione 165 mmHg, febbrile 38.5°C
mario_rossi = np.array([[78.0, 125.0, 88.0, 165.0, 38.5]])
prob_crisi = model.predict_proba(mario_rossi)[0, 1]

# 4. Calcolo SHAP: dissezione algebrica della decisione
t0 = time.perf_counter()
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(mario_rossi)
t_shap_ms = (time.perf_counter() - t0) * 1000

# Nel caso binario, prendiamo i contributi verso la classe 1 (crisi cardiaca)
# (Gestione compatibilità output SHAP per scikit-learn)
if isinstance(shap_values, list):
    valori_paziente = shap_values[1][0]
    base_val = explainer.expected_value[1]
elif len(shap_values.shape) == 3:
    valori_paziente = shap_values[0, :, 1]
    base_val = explainer.expected_value[1]
else:
    valori_paziente = shap_values[0]
    base_val = explainer.expected_value

print(f"--- PRESTAZIONI ---")
print(f"Tempo Training: {t_train_ms:.2f} ms")
print(f"Tempo Spiegazione SHAP (Inferenza + Dissezione): {t_shap_ms:.2f} ms\n")

print(f"--- MONITOR TERAPIA INTENSIVA ---")
print(f"Diagnosi Paziente: RISCHIO CRISI = {prob_crisi * 100:.1f}%")
print(f"Rischio di base medio della popolazione: {base_val * 100:.1f}%\n")

print(f"--- DISSEZIONE CAUSALE (I biomarcatori responsabili) ---")
# Ordiniamo i fattori dal più impattante al meno impattante
indici_ordinati = np.argsort(np.abs(valori_paziente))[::-1]

for idx in indici_ordinati:
    nome = feature_names[idx]
    valore_reale = mario_rossi[0, idx]
    impatto = valori_paziente[idx]
    segno = "+" if impatto > 0 else ""
    direzione = "AUMENTA IL RISCHIO" if impatto > 0 else "RIDUCE IL RISCHIO"
    print(f"{nome:<20} = {valore_reale:>6.1f}  --> Impatto: {segno}{impatto*100:>5.1f}%  ({direzione})")
