import torch
import torch.nn as nn
import torch.optim as optim

# 1. Dati non lineari: parabola y = x^2 (con rumore)
torch.manual_seed(42)
X = torch.linspace(-3.0, 3.0, 200).unsqueeze(1) # 200 punti tra -3 e 3
y_true = X ** 2 + torch.randn_like(X) * 0.2

# 2. La Rete Neurale: Due strati di manopole con un interruttore in mezzo
# Entra 1 numero -> 16 neuroni nascosti -> esce 1 numero
modello = nn.Sequential(
    nn.Linear(1, 16),  # Mixer 1: crea 16 combinazioni lineari diverse
    nn.ReLU(),         # Interruttore: taglia i negativi a zero (piega la retta)
    nn.Linear(16, 1)   # Mixer 2: ricombina i 16 segnali piegati in un'unica uscita
)

# 3. Errore e Ottimizzatore industriale (Adam: muove le manopole con slancio)
criterio_loss = nn.MSELoss()
ottimizzatore = optim.Adam(modello.parameters(), lr=0.05)

# 4. Il Loop di Addestramento
for epoca in range(300):
    # A. Forward: spara la predizione
    y_pred = modello(X)

    # B. Loss: calcola lo scarto quadratico
    loss = criterio_loss(y_pred, y_true)

    # C. Zero grad: cancella il taccuino
    ottimizzatore.zero_grad()

    # D. Backward: calcola all'indietro le colpe di tutti i 16+1 neuroni
    loss.backward()

    # E. Step: la mano gira tutte le manopole insieme
    ottimizzatore.step()

    if (epoca + 1) % 60 == 0:
        print(f"Epoca {epoca+1:03d} | Errore (Loss): {loss.item():.4f}")
