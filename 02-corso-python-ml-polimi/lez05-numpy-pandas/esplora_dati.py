from medmnist import PneumoniaMNIST
import sys
from pathlib import Path


DATI = Path(__file__).resolve().parent / "dati"
ds = PneumoniaMNIST(split="train", download=True, root=DATI)

print("Immagini nel train:", ds.imgs.shape[0])
immagine = ds.imgs[0]
print("Forma:", immagine.shape)
print("Tipo:", immagine.dtype)
