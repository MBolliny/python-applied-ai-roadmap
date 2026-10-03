from typing import List, Optional


class ReadingBuffer:
    """Contenitore per memorizzare e confrontare serie temporali di un sensore.

    Riceve:
        sensor_name (str): Identificativo del canale di acquisizione.
        readings (list[float], opzionale): Lista iniziale di campioni numerici.
    """

    def __init__(self, sensor_name: str, readings: Optional[List[float]] = None
    ) -> None:
        
        self.sensor_name = sensor_name

        # Gestione del default mutabile: se non viene passata, creiamo una lista nuova
        if readings is None:
            self.lista_letture = []
        else:
            self.lista_letture = list(readings)

    def add_reading(self, value: float) -> None:
        """Aggiunge una nuova misura in coda alla serie temporale."""
        self.lista_letture.append(float(value))

    def __len__(self) -> int:
        """Permette a Python di chiamare len(oggetto) contando gli elementi salvati."""
        return len(self.lista_letture)

    def __str__(self) -> str:
        """Restituisce il testo sintetico per l'operatore a schermo."""
        conteggio = len(self.lista_letture)
        return f"Sensor {self.sensor_name}: {conteggio} readings"

    def __repr__(self) -> str:
        """Restituisce la rappresentazione tecnica non ambigua per il debug."""
        return f"ReadingBuffer(sensor_name='{self.sensor_name}', readings={self.lista_letture})"

    def __eq__(self, altro_oggetto: object) -> bool:
        """Determina se due buffer hanno lo stesso nome sensore e gli stessi identici dati."""
        # Controllo di tipo: se l'altro oggetto non è un ReadingBuffer, sono diversi
        if not isinstance(altro_oggetto, ReadingBuffer):
            return False

        # Verifica di identità logica: stesso sensore e sequenza identica
        stesso_nome = self.sensor_name == altro_oggetto.sensor_name
        stessi_dati = self.lista_letture == altro_oggetto.lista_letture

        return stesso_nome and stessi_dati