# spostamento nella cartella per importazine
from pathlib import Path
import sys

percorso_test = Path(__file__).resolve()
cartella_progetto = percorso_test.parent.parent
cartella_sorgenti = cartella_progetto / "src"
sys.path.append(str(cartella_sorgenti))

from paziente import Paziente

# creazione paziente
paziente_zero = Paziente("Mario Rossi")
print(paziente_zero.identificativo_paziente)
