import matplotlib.pyplot as plt
import numpy as np

# 1. Prepariamo due liste di numeri banali (asse X e asse Y)
giorni = [1, 2, 3, 4, 5]
ore_studio = [2, 3, 1, 4, 5]

# 2. Disegniamo un grafico a linee (il comando più classico di Matplotlib)
plt.plot(giorni, ore_studio, marker="o", color="blue")

# 3. Aggiungiamo le scritte intorno al grafico
plt.title("Le mie ore di studio")  # Titolo in alto
plt.xlabel("Giorno della settimana")  # Etichetta asse orizzontale (X)
plt.ylabel("Ore")  # Etichetta asse verticale (Y)
plt.grid(True)  # Mostra la griglia a quadretti sullo sfondo

# 4. Mostriamo il risultato a schermo
plt.show()
