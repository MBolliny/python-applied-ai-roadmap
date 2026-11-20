import torch

# 1. Dati finti: legge fisica sottostante y = 3.0 * x + 2.0
torch.manual_seed(42)
X = torch.linspace(-2.0, 2.0, 100).unsqueeze(1) # Matrice 100x1
y_true = 3.0 * X + 2.0 + torch.randn_like(X) * 0.1 # Con un po' di rumore

# 2. Le Manopole del Modello (pesi inizializzati a caso)
w = torch.randn(1, 1, requires_grad=True)
b = torch.zeros(1, requires_grad=True)

print(f"Pesi iniziali a caso -> w: {w.item():.4f}, b: {b.item():.4f}")

# 3. Iperparametri
learning_rate = 0.1
epochs = 50

# 4. Il Loop di Addestramento
for epoch in range(epochs):
    # A. FORWARD PASS: la predizione
    y_pred = X @ w + b  # Prodotto matrice-vettore

    # B. CALCOLO DELLA LOSS (Mean Squared Error: scarto quadratico medio)
    loss = torch.mean((y_pred - y_true) ** 2)

    # C. BACKWARD PASS: lo spotter riempie i taccuini w.grad e b.grad
    loss.backward()

    # D. OPTIMIZER STEP (aggiornamento delle manopole)
    # torch.no_grad() serve per dire: "non tracciare questa sottrazione nel grafo!"
    with torch.no_grad():
        w -= learning_rate * w.grad
        b -= learning_rate * b.grad

    # E. ZERO GRAD: cancella il taccuino con la gomma
    w.grad.zero_()
    b.grad.zero_()

    if (epoch + 1) % 10 == 0:
        print(f"Epoca {epoch+1:02d} | Loss: {loss.item():.6f} | w: {w.item():.4f}, b: {b.item():.4f}")

print(f"\nRisultato finale -> w: {w.item():.4f} (target 3.0), b: {b.item():.4f} (target 2.0)")
