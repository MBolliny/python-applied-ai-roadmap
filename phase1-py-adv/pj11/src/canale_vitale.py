class CanaleVitale:

    def __init__(self, identificativo, misura, valore_minimo, valore_massimo):
        self.identificativo = identificativo
        self.misura = misura
        self.valore_minimo = valore_minimo
        self.valore_massimo = valore_massimo
        self.storico_dati = []

    def registra_campione(self, valore):
        if  valore < self.valore_minimo or valore > self.valore_massimo:
            print(f"[SCARTATO] {self.identificativo}: Valore {valore} fuori soglia ")
            return

        self.storico_dati.append(valore)




