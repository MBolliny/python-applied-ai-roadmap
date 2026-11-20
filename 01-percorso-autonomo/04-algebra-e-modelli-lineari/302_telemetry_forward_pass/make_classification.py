from sklearn.datasets import make_classification
import numpy as np

X, y = make_classification(
    n_samples=10_000,
    n_features=20,
    n_informative=5,
    random_state=42
)
