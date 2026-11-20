
import sys

def verifica_saturazione(spo2: int) -> int:
    assert 0 <= spo2 <= 100, "La saturazione deve essere compresa tra 0 e 100"

    if spo2 <= 91:
        return 3
    if 92 <= spo2 <= 93:
        return 2
    if 94 <= spo2 <= 95:
        return 1
    return 0

def verifica_saturazione_bcpo(spo2: int, ossigeno: bool = False) -> int:
    assert 0 <= spo2 <= 100, "La saturazione deve essere compresa tra 0 e 100"

    if spo2 <= 83 or (spo2 >= 97 and ossigeno):
        return 3
    if (84 <= spo2 <= 85) or (95 <= spo2 <= 96 and ossigeno):
        return 2
    if (86 <= spo2 <= 87) or (93 <= spo2 <= 94 and ossigeno):
        return 1
    return 0

    # lista valori
    spo2_bcpo = {
            (91, 91): 0,
            (92, 93): 1,
            (94, 95): 2,
            (96, 96): 3
            }

    for (min_val, max_val), punti in spo2_bcpo.items():
        if min_val <= saturazione <= max_val:
            return punti

def verifica_respiratoria(freq_resp: int)-> int:

    assert freq_resp >= 0, "La frequenza respiratoria non può essere negativa"

    if freq_resp <= 8 or freq_resp >= 25:
        return 3
    if 21 <= freq_resp <= 24:
        return 2
    if 9 <= freq_resp <= 11:
        return 1
    if 12 <= freq_resp <= 20:
        return 0

def verifica_cardiaca(freq_card: int) -> int:
  assert freq_card >= 0, "La frequenza cardiaca non può essere negativa"

  if freq_card <= 40 or freq_card >= 131:
    return 3
  if 111 <= freq_card <= 130:
    return 2
  if (41 <= freq_card <= 50) or (91 <= freq_card <= 110):
    return 1
  if 51 <= freq_card <= 90:
    return 0

def valuta_rischio(punti: int):

    # assert punti < 0, "punti minori di 0"

    if 0 <= punti <= 4:
        return "BASSO"

    if punti == 5 or punti == 6:
            return "MEDIO"

    return "ALTO"

if __name__ == "__main__":

    # conversione
    argomenti = []
    bcpo = False
    for i in range(1,len(sys.argv)-1):
        if sys.argv[i] == "bcpo":
            bcpo = True
            argomenti.append(sys.argv[i])
        else:
            argomenti.append(int(sys.argv[i]))
    print (argomenti)

    if bcpo:
       punti_sat = verifica_saturazione_bcpo(argomenti[0])
    else:
        punti_sat = verifica_saturazione(argomenti[0])

    punti = punti_sat + verifica_respiratoria(argomenti[1]) + verifica_cardiaca(argomenti[2])

    # valutazione rischio
    rischio = valuta_rischio(punti)
    print(f"punteggio: {punti} - rischio: {rischio}")
