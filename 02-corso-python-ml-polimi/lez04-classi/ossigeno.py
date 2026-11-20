'''
Da sistemare
- aggingere classi create in una lista
- stampare il nome della classe creata
- Passare parametri con il self

Imparato
- accedp a valori nella classe con self. (d'apperitto)
- creazione classe non ha chiamata a funzione come le altre => classe.n() o =classe()'''

class Flebo:
    def __init__(self, farmaco, velocita, volume):

        if velocita <= 0 or volume <= 0:
           raise ValueError("Volume e velocità devono essere maggiori di zero!")

        if not medicinale or not medicinale.strip():
            raise ValueError("Il nome della flebo non può essere vuoto!")

        self.letto = lettofarmaco
        self.farmaco = medicinale
        self.volume = volume
        self.velocita = velocita


    def calcolo_ore(self, velocita, volume):
        return self.volume / self.velocita

if __name__ == "__main__":


    for flebo in FLEBO_DEL_TURNO:

        try:
            # creazione classe
            nuova_flebo = Flebo(nome = flebo[0], volume = flebo[1], velocita = flebo[2])
            class_list.append(nuova_flebo)


            # calcolo valori
            ore = nuova_flebo.calcolo_ore(volume, velocita)
            print(f"{nuova_flebo} -> Durata: {ore} ore")

        except ValueError as errore:
            continue
        # calcolo ora
        print(class_list)

