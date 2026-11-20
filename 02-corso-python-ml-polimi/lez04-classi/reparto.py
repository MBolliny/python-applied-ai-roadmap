class Bombola:

    def __init__(self, letto: int, paziente: str, volume: int, velocita = int):

        if velocita <= 0 or volume <= 0:
           raise ValueError("Volume e velocità devono essere maggiori di zero!")

        if not paziente or not paziente.strip():
            raise ValueError("Il nome del paziente non può essere vuoto!")

        self.letto = letto
        self.paziente = paziente
        self.volume = volume
        self.velocita = velocita

    def minuti_rimanenti(self) -> int:
        return self.volume / self. velocita

    def volume_consumato(self, tempo) -> int:
        return tempo *  self.velocita

    #def aggiorna_utilizzo(self):


if __name__ == "__main__":

    # inizializzazione e dati
    BOMBOLE_INIZIO_TURNO = [
        {"letto": 12, "paziente": "Rossi",   "litri": 600, "flusso_l_min": 2},
        {"letto": 7,  "paziente": "Bianchi", "litri": 300, "flusso_l_min": 5},
        {"letto": 3,  "paziente": "Verdi",   "litri": 400, "flusso_l_min": 4},
        {"letto": 9,  "paziente": "",        "litri": 500, "flusso_l_min": 3},
    ]

    diz_bombole: dict = {}
    diz_tempi: dict = {}

    # lettura di ogni caratteristica delle bombole
    for rapporto_bombole in BOMBOLE_INIZIO_TURNO:

        letto = rapporto_bombole.get("letto", "Non trovata")
        paziente = rapporto_bombole.get("paziente", "Non trovata")
        volume = rapporto_bombole.get("litri", "Non trovata")
        velocita = rapporto_bombole.get("flusso_l_min", "Non trovata")

        try:
            # creazione + verifica (interna) delle bombole
            bombola = Bombola(velocita= velocita, paziente= paziente, letto= letto, volume= volume)

            # creazione del dizionario
            diz_bombole[letto] = bombola
            diz_tempi[letto] = bombola.minuti_rimanenti()

        except ValueError as errore:
            continue

    print(f"tempo = 60min")
    print(diz_tempi)

    count_ora = 60
    flag_bombola_finita = False

    while not flag_bombola_finita:

        minuti = 60

        for letto, classe_bombola in diz_bombole.items():

            # verifica se il volume rimanente basta per un'ora
            if classe_bombola.volume < classe_bombola.volume_consumato(tempo=minuti):
                flag_bombola_finita = True
                break

            # aggiornamento variabili bombola
            classe_bombola.volume -= classe_bombola.volume_consumato(tempo=minuti)
            tempo_rimanente = classe_bombola.minuti_rimanenti()
            diz_tempi[letto] = tempo_rimanente

            # verifica se qualcuno sia finito
            if tempo_rimanente <= 0:
                flag_bombola_finita = True

        # stampa solo se l'ora intera è stata completata
        if not flag_bombola_finita:
            print(f"tempo = {count_ora}min")
            print(diz_tempi)
            count_ora += minuti

    # output e stamp

