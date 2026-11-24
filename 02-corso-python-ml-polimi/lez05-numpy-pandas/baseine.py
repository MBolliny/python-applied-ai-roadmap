from medmnist import PneumoniaMNIST
from pathlib import Path
import numpy as np

DATI = Path(__file__).resolve().parent / "dati"

ds_train = PneumoniaMNIST(split="train", download=False, root=DATI)
ds_test = PneumoniaMNIST(split="test", download=False, root=DATI)
ds_val = PneumoniaMNIST(split="val", download=False, root=DATI)

dataset_completo = [ds_train, ds_test, ds_val]

for oggetto in dataset_completo:
    # estraggo array
    array_labels = oggetto.labels.ravel()
    print(f"Dimensione array: {array_labels.size}")

    # Conteggio rapido dei malati (1) e sani (0)
    malati = (array_labels == 1).sum()
    salute = array_labels.size - malati
    print(f"Malati: {malati} | Sani: {salute}")

    # Calcolo della baseline
    baseline = (max(malati, salute) / array_labels.size) * 100

    # Stampa arrotondata (scegli quella che preferisci):
    print(f"Baseline (intero arrotondato): {round(baseline)}%")
    print(f"Baseline (2 decimali): {baseline:.2f}%")


