from pathlib import Path
import matplotlib.pyplot as plt
from medmnist import PneumoniaMNIST

DATI = Path(__file__).resolve().parent / "dati"
ds = PneumoniaMNIST(split="train", download=False, root=DATI)

indice = 0  # Cambia questo numero per vedere altre radiografie

immagine = ds.imgs[indice]  # Forma: (28, 28)
etichetta = ds.labels[indice].item()  # Estrae il valore intero: 0 oppure 1

diagnosi = "Polmonite (Malato)" if etichetta == 1 else "Sano"

plt.imshow(immagine, cmap="gray")
plt.title(f"Radiografia #{indice} - {diagnosi} ({etichetta})")
plt.axis("off")
plt.show()
