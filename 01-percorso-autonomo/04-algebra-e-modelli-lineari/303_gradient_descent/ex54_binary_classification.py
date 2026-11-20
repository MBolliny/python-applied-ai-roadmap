import torch
import torch.nn as nn
import torch.optim as optim

# 1. Dataset finto: 2 biomarcatori (X) per paziente
torch.manual_seed(42)
# 100 Pazienti sani (classe 0): valori bassi attorno a (2, 2)
sani = torch.randn(100, 2) + torch.tensor([2.0, 2.0])
# 100 Pazienti a rischio (classe 1): valori alti attorno a (5, 5)
malati = torch.randn(100, 2) + torch.tensor([5.0, 5.0])

X = torch.cat([sani, malati], dim=0) # Matrice 200x2
y_true = torch.cat([torch.zeros(100, 1), torch.ones(100, 1)], dim=0) # 200x1 (etichette 0 e 1)

# 2. Modello di Classificazione: Mixer -> Sigmoide
modello_clinico = nn.Sequential(
    nn.Linear(2, 1), # Entrano 2 sensori, esce 1 punteggio grezzo z
    nn.Sigmoid()     # Schiaccia il punteggio z tra 0.0 e 1.0 (Probabilità)
)

# 3. Funzione di errore per probabilità (Binary Cross-Entropy) e Ottimizzatore
criterio_loss = nn.BCELoss()
ottimizzatore = optim.SGD(modello_clinico.parameters(), lr=0.2)

# 4. Training Loop
for epoca in range(100):
    # Forward: esce una probabilità tra 0 e 1
    probabilita = modello_clinico(X)

    # Loss: calcola la penalità logaritmica
    loss = criterio_loss(probabilita, y_true)

    # Backward e Step
    ottimizzatore.zero_grad()
    loss.backward()
    ottimizzatore.step()

    if (epoca + 1) % 25 == 0:
        predizioni_binarie = (probabilita >= 0.5).float()
        accuratezza = (predizioni_binarie == y_true).float().mean() * 100
        print(f"Epoca {epoca+1:03d} | Loss: {loss.item():.4f} | Accuratezza: {accuratezza:.1f}%")

# 5. Test su due nuovi pazienti in ingresso
paziente_A = torch.tensor([[1.5, 1.8]]) # Valori bassi
paziente_B = torch.tensor([[6.2, 5.8]]) # Valori alti

with torch.no_grad():
    print(f"\nPaziente A (1.5, 1.8) -> Rischio calcolato: {modello_clinico(paziente_A).item()*100:.1f}%")
    print(f"Paziente B (6.2, 5.8) -> Rischio calcolato: {modello_clinico(paziente_B).item()*100:.1f}%")
