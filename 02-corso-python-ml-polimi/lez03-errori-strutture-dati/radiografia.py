import random

def verifica_radiografia(radiografia: int):

    # verifica dimensione
    lunghezza_righe = len(radiografia)
    for colonna in radiografia:
        lunghezza_colonna = len(colonna)
        if  lunghezza_colonna != lunghezza_righe:
            raise ValueError(f"matrice non rettangolare - {lunghezza_righe}x{lunghezza_colonna}")

    # verifica pixel
    for riga in radiografia:
        for pixel in riga:
            if pixel > 255 or pixel < 0:
                raise ValueError(f"valore pixel {pixel} esce dal range")

def genera_indici_casuali(grandezza_matrice):
    inizio_righe = random.randint(0, grandezza_matrice - 1)
    fine_righe = random.randint(inizio_righe + 1, grandezza_matrice)

    inizio_colonne = random.randint(0, grandezza_matrice - 1)
    fine_colonne = random.randint(inizio_colonne + 1, grandezza_matrice)

    return inizio_righe, fine_righe, inizio_colonne, fine_colonne

def estrai_sottomatrice(matrice, in_r, fine_r, in_c, fine_c):
    sottomatrice = []
    sotto_righe = matrice[in_r:fine_r]

    for riga in sotto_righe:
        sottocolonne = riga[in_c:fine_c]
        sottomatrice.append(sottocolonne)

    return sottomatrice

def analizza_sottomatrice(sottomatrice):
    righe = len(sottomatrice)
    colonne = len(sottomatrice[0]) if righe > 0 else 0

    dimensione = righe * colonne
    somma_totale = sum(sum(riga) for riga in sottomatrice)
    media = somma_totale / dimensione if dimensione > 0 else 0

    return dimensione, media

# input e dati

SEMPLICE = [
    [3, 9, 5, 6],
    [1, 4, 9, 2],
    [3, 6, 2, 1],
    [1, 6, 8, 4],
]

# l'immagine buona
IMMAGINE_BUONA = [
    [10, 12, 15, 14, 11, 10],
    [12, 80, 95, 90, 70, 13],
    [14, 85, 200, 210, 75, 12],
    [13, 90, 205, 220, 80, 14],
    [11, 70, 88, 92, 65, 12],
    [10, 11, 13, 12, 11, 10],
]

# tre immagini rotte, ognuna con un problema diverso
IMMAGINE_RIGA_CORTA = [
    [10, 12, 15, 14, 11, 10],
    [12, 80, 95, 90, 70, 13],
    [14, 85, 200, 210, 75, 12],
    [13, 90, 205, 220, 80],        # manca un pixel
    [11, 70, 88, 92, 65, 12],
    [10, 11, 13, 12, 11, 10],
]

IMMAGINE_PIXEL_ROTTO = [
    [10, 12, 15, 14, 11, 10],
    [12, 80, 95, 90, 70, 13],
    [14, 85, -3, 210, 75, 12],    # 300 non esiste, il massimo è 255
    [13, 90, 205, 220, 80, 14],
    [11, 70, 88, 92, 65, 12],
    [10, 11, 13, 12, 11, 10],
]

IMMAGINE_VUOTA = []

# inizializzazione
matrice = IMMAGINE_BUONA
sottomatrice: list = []
vettore_somme: list = []

# verifiche
verifica_radiografia(IMMAGINE_RIGA_CORTA)

# elaborazione
grandezza = len(matrice)
in_r, fine_r, in_c, fine_c = genera_indici_casuali(grandezza)

print(f"Righe: {in_r}-{fine_r - 1}, Colonne: {in_c}-{fine_c - 1}")

sub = estrai_sottomatrice(matrice, in_r, fine_r, in_c, fine_c)
dimensione, media = analizza_sottomatrice(sub)

print("Sottomatrice:", sub)
print(f"Elementi totali: {dimensione}")
print(f"Media: {media:.2f}")









# output
