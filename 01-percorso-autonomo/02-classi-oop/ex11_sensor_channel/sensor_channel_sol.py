class channelSensor:
    """Rappresenta un singolo canale di misura.
    
    Riceve un identificativo testuale e un valore numerico iniziale.
    Permette di aggiornare il valore solo se maggiore o uguale a zero.
    """

    def __init__(self, identificativo: str, valore_iniziale: float) -> None:
        self.identificativo = identificativo
        # Facciamo passare anche il dato iniziale dalla funzione di controllo
        self.imposta_valore(valore_iniziale)

    def imposta_valore(self, nuovo_valore: float) -> None:
        """Aggiorna il dato memorizzato solo se rispetta il vincolo fisico."""
        if nuovo_valore < 0:
            raise ValueError(f"Valore non valido: {nuovo_valore} (deve essere >= 0)")

        self.valore = nuovo_valore