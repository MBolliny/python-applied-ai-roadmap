import random
from cohort_analyzer import analizza_coorti

def calcola_atteso(gruppo_a, gruppo_b, telemetria=None, soglia=0.0):
    """Oracolo indipendente per validare qualsiasi input."""
    set_a = set(gruppo_a)
    set_b = set(gruppo_b)

    out = {
        "comuni": set_a.intersection(set_b),
        "esclusivi": set_a.symmetric_difference(set_b),
        "totali": set_a.union(set_b),
    }

    if telemetria is not None:
        sopra = []
        for pz, letture in telemetria.items():
            finestra = letture[-3:]
            media = sum(finestra) / len(finestra)
            if media > soglia:
                sopra.append(pz)
        out["sopra_soglia"] = sopra

    return out


def esegui_test_dinamici(fn_da_testare, num_round=10):
    verde = "\033[92m"
    rosso = "\033[91m"
    reset = "\033[0m"

    pazienti_pool = [f"PAT-{i:02d}" for i in range(1, 25)]
    superati = 0

    print(f"\n--- AVVIO TEST DINAMICI ({num_round} ROUND RANDOMIZZATI) ---")

    for i in range(1, num_round + 1):
        # 1. Genera liste pazienti A e B casuali
        k_a = random.randint(3, 7)
        k_b = random.randint(3, 7)
        a = random.sample(pazienti_pool, k_a)
        b = random.sample(pazienti_pool, k_b)

        # 2. Genera telemetria casuale con 3-8 campioni per paziente
        tutti_pazienti = list(set(a) | set(b))
        telemetria = {}
        for p in tutti_pazienti:
            n_campioni = random.randint(3, 8)
            telemetria[p] = [round(random.uniform(5.0, 50.0), 2) for _ in range(n_campioni)]

        # 3. Imposta soglia casuale centrata sui dati
        soglia = round(random.uniform(15.0, 35.0), 2)

        atteso = calcola_atteso(a, b, telemetria, soglia)

        try:
            ottenuto = fn_da_testare(a, b, telemetria=telemetria, soglia=soglia)

            assert ottenuto.get("comuni") == atteso["comuni"], (
                f"Comuni errati: {ottenuto.get('comuni')} != {atteso['comuni']}"
            )
            assert ottenuto.get("esclusivi") == atteso["esclusivi"], (
                f"Esclusivi errati: {ottenuto.get('esclusivi')} != {atteso['esclusivi']}"
            )
            assert ottenuto.get("totali") == atteso["totali"], (
                f"Totali errati: {ottenuto.get('totali')} != {atteso['totali']}"
            )

            # Controllo sopra_soglia (confronto come insiemi per evitare errori di ordinamento puro)
            atteso_sopra = set(atteso["sopra_soglia"])
            ottenuto_sopra = set(ottenuto.get("sopra_soglia", []))
            assert ottenuto_sopra == atteso_sopra, (
                f"Sopra soglia errato con soglia={soglia}:\n"
                f"  Ottenuto: {ottenuto.get('sopra_soglia')}\n"
                f"  Atteso:   {atteso['sopra_soglia']}"
            )

            print(f"[{verde}PASS{reset}] Round {i:02d}: {len(tutti_pazienti)} pazienti, soglia={soglia:.2f}")
            superati += 1

        except AssertionError as err:
            print(f"[{rosso}FAIL{reset}] Round {i:02d} -> {err}")
            break
        except Exception as e:
            print(f"[{rosso}CRASH{reset}] Round {i:02d} -> Errore runtime: {e}")
            break

    print(f"\nEsito: {superati}/{num_round} superati con dati dinamici.\n")


# Incolla qui sotto la tua analizza_coorti oppure importala:
if __name__ == "__main__":
    esegui_test_dinamici(analizza_coorti)