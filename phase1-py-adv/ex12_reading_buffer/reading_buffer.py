
class ReadingBuffer:

    def __init__(self, canale, dati):
            self.canale = canale
            self.dati = dati

        def __eq__(self, classe_da_verificare):
            # 1. Se 'altro' non è un'istanza di BufferMinimo, ritorna False
            # 2. Ritorna True se sia il canale che i dati sono identici
            pass