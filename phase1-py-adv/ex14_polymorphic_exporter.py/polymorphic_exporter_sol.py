from abc import ABC, abstractmethod
import csv
import json
from pathlib import Path


class EsportatoreBase(ABC):
    """Classe base astratta che definisce il contratto comune per tutti gli esportatori.

    Riceve:
        percorso_uscita (str | Path): Destinazione del file da generare.
    """

    def __init__(self, percorso_uscita: str | Path) -> None:
        self.destinazione = Path(percorso_uscita)

    @abstractmethod
    def export(self, lista_dati: list[dict[str, float | str]]) -> Path:
        """Metodo astratto: ogni classe figlia è obbligata a implementarlo."""
        pass


class EsportatoreCSV(EsportatoreBase):
    """Esporta serie di dati tabulari in formato CSV con intestazioni."""

    def export(self, lista_dati: list[dict[str, float | str]]) -> Path:
        """Salva i dizionari su file CSV.

        Solleva:
            ValueError: Se la lista di dati è vuota.
        """
        if not lista_dati:
            raise ValueError("Records list cannot be empty")

        # Assicuriamo che la cartella genitore esista sul disco
        self.destinazione.parent.mkdir(parents=True, exist_ok=True)

        # Usiamo le chiavi del primo elemento come colonne del CSV
        nomi_colonne = list(lista_dati[0].keys())

        with open(
            self.destinazione, mode="w", newline="", encoding="utf-8"
        ) as file_disco:
            scrittore = csv.DictWriter(file_disco, fieldnames=nomi_colonne)
            scrittore.writeheader()
            scrittore.writerows(lista_dati)

        return self.destinazione


class EsportatoreJSON(EsportatoreBase):
    """Esporta serie di dati complessi o gerarchici in formato JSON strutturato."""

    def export(self, lista_dati: list[dict[str, float | str]]) -> Path:
        """Salva i dizionari su file JSON.

        Solleva:
            ValueError: Se la lista di dati è vuota.
        """
        if not lista_dati:
            raise ValueError("Records list cannot be empty")

        self.destinazione.parent.mkdir(parents=True, exist_ok=True)

        with open(self.destinazione, mode="w", encoding="utf-8") as file_disco:
            json.dump(lista_dati, file_disco, indent=2)

        return self.destinazione