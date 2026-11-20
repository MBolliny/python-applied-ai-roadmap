class CanaleVitale:

    def __init__(self, identificativo, misura, range):
        self.identificativo = identificativo
        self.misura = misura
        self.valore_minimo = range[0]
        self.valore_massimo = range[1]
        self.storico_dati = []

    def registra_campione(self, valore):
        '''
            aggiunta campione al report dopo controllo di verifica idoneita'

            args
            - valore da aggiungere
        '''

        # verifica tipo
        if not isinstance(valore, (int, float)) and isinstance(valore, (bool)):
            raise TypeError({valore}, "e' di tipo sbagliato")

        # verifica range appartenenza
        if not (self.valore_minimo <= valore <= self.valore_massimo):
            raise ValueError({valore}, "fuori range")

        # aggiunta valore a report
        self.storico_dati.append(valore)

    def calcola_statistiche(self) -> [float, float]:
        '''
        calcolo max e media dal report dati della classe
        '''

        # verifica preventiva per la media
        if not self.storico_dati:
            print("lista vuota - media non calcolabile")
            return (0.0, 0.0)

        max = self.storico_dati[0]
        sum = 0.0
        count = 0

        # singolo scorrimento della lista
        for measure in self.storico_dati:

            # aggiorno max
            if measure > max:
                max = measure

            # calcolo media
            count += 1
            sum += measure

        media = sum / float(count)

        return (max, media)

    def __len__(self):
        return len(self.storico_dati)
