from pathlib import Path
import csv

class CSVRecordParser:
    """Legge un file CSV e restituisce una lista di dizionari."""
    def parse(self, file_path: Path) -> list[dict]:

        record = []

        # apro il file
        with file_path.open("r", encoding="utf-8") as f:

            # trasformazione in dizionario
            reader = csv.DictReader(f)

            for riga in reader:
                record.append(dict(riga))
                print(riga)

            print(record)
            return record


class KeyValueRecordParser:
    """Legge un file .kv (chiave=valore) e restituisce una lista di dizionari."""
    def parse(self, file_path: Path) -> list[dict]:
        dizionario: dict = {}

        with file_path.open("r", encoding="utf-8") as f:
            for riga in f:
                linea = riga.strip()

                # Salta righe vuote o commenti
                if not linea or linea.startswith("#"):
                    continue

                # Gestione solo delle righe che contengono il separatore
                if "=" in linea:
                    chiave, valore = linea.split("=", 1)
                    dizionario[chiave.strip()] = valore.strip()

        # Restituisce una lista con dentro il dizionario (se non vuoto)
        return [dizionario] if dizionario else []
