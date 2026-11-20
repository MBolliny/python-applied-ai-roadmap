
if __name__ == "__main__":

    # inizializzazione
    diz_letture = {}
    file_da_leggere = "/Users/MatteoBollini/Documents/Python-projects/found-to-ML/lez04-classi/letture.csv"
    count_righe_vuote = 0

    # elaborazione
    try:
        with open(file_da_leggere, "r", encoding="utf-8") as file_pointer:
            for riga in file_pointer:

                # verifica pulizia della riga
                riga_pulita = riga.strip()
                if not riga_pulita:
                    count_righe_vuote += 1
                    continue

                # elaborazione e verifica del dato
                riga_separata = riga_pulita.split(",")

                try:
                    paziente = str(riga_separata[-2])
                    saturazione = int(riga_separata[-1])

                    somma_valori, count_valori = diz_letture.get(paziente, (0, 0))
                    diz_letture[paziente] = (somma_valori + saturazione, count_valori + 1)

                except ValueError:
                    print(f"Errore: '{riga_separata[-1]}'")

        # visualizzazion media
        for paziente, (somma_totale, count_misure) in diz_letture.items():
            print(f"{paziente}: {float(somma_totale)/ count_misure}")
        print(f"righe_vuote: {count_righe_vuote}")

    except FileNotFoundError:
        print("file non esistente")

