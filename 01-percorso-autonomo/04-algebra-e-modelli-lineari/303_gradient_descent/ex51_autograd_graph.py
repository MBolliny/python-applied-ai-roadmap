import torch

# 1. Foglia sorgente con tracciamento del grafo abilitato
x = torch.tensor([1.0, 2.0, 3.0, 4.0], requires_grad=True)
print(f"1. Input x: {x}")

# 2. Forward pass: operazione algebrica e riduzione a scalare unico
y = torch.sum(3 * (x ** 2) + 2 * x)
print(f"2. Scalare y: {y.item()} | Nodo radice (grad_fn): {y.grad_fn}")

# 3. Primo Backward pass: calcolo dei gradienti dy/dx
y.backward()
print(f"3. Gradiente calcolato in memoria (x.grad): {x.grad}")
grad_analitico = 6 * x.detach() + 2
print(f"   Gradiente analitico atteso (6x + 2):    {grad_analitico}")

# 4. Secondo Backward pass SENZA azzeramento: accumulo sul taccuino
y2 = torch.sum(3 * (x ** 2) + 2 * x)
y2.backward()
print(f"4. Gradiente dopo secondo backward (ACCUMULO): {x.grad}")

# 5. Reset manuale del taccuino (operazione in-place)
x.grad.zero_()
print(f"5. Gradiente dopo x.grad.zero_(): {x.grad}")
