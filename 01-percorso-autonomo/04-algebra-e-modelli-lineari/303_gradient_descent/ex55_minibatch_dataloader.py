import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

# 1. Creazione di un Dataset personalizzato
class SegnaliPazientiDataset(Dataset):
    def __init__(self, num_pazienti=1000):
        # 1000 pazienti, ognuno con 4 biomarcatori
        torch.manual_seed(42)
        self.X = torch.randn(num_pazienti, 4)
        # Etichetta: 1 se la somma supera 0.5, altrimenti 0
        self.y = (self.X.sum(dim=1, keepdim=True) > 0.5).float()

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        # Restituisce la singola coppia (input, target)
        return self.X[idx], self.y[idx]

# 2. Inizializzazione Dataset e DataLoader
dataset_completo = SegnaliPazientiDataset(num_pazienti=1000)

# Batch size = 32 -> 1000 / 32 = 31.25 -> 32 pacchetti per epoca
train_loader = DataLoader(dataset_completo, batch_size=32, shuffle=True)

# 3. Modello compatto
modello = nn.Sequential(
    nn.Linear(4, 8),
    nn.ReLU(),
    nn.Linear(8, 1),
    nn.Sigmoid()
)

criterio = nn.BCELoss()
ottimizzatore = torch.optim.Adam(modello.parameters(), lr=0.01)

# 4. Training Loop a due livelli: Epoche e Batch
num_epoche = 5

for epoca in range(num_epoche):
    loss_cumulata_epoca = 0.0

    # Il DataLoader sputa fuori un batch alla volta
    for batch_idx, (batch_X, batch_y) in enumerate(train_loader):
        # 1. Forward
        pred = modello(batch_X)
        loss = criterio(pred, batch_y)

        # 2. Backward & Step (per ogni singolo pacchetto da 32!)
        ottimizzatore.zero_grad()
        loss.backward()
        ottimizzatore.step()

        loss_cumulata_epoca += loss.item()

    loss_media = loss_cumulata_epoca / len(train_loader)
    print(f"Epoca {epoca+1:02d} completata | Pacchetti elaborati: {len(train_loader)} | Loss media: {loss_media:.4f}")
