class Paziente:
    """Rappresenta un paziente monitorato e aggrega i suoi canali vitali."""

    def __init__(self, identificativo_paziente):
        self.identificativo_paziente = identificativo_paziente
        # Dizionario interno vuoto: conterrà coppie 'ID_CANALE': oggetto_canale
        self.canali = {}

    def collega_canale(self, canale_da_aggiungere):
        self.canali[canale_da_aggiungere.identificativo] = canale_da_aggiungere

