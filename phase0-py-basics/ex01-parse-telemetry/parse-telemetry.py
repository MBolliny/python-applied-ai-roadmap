
def parse_telemetria(raw_string: str) -> tuple[int, float, str]:
    """
    Funzione che prende in input una riga grezza di telemetria e restituisce una tupla contenente:
    - un intero rappresentante l'ID del sensore
    - un float rappresentante il valore della telemetria
    - una stringa rappresentante l'unità di misura

    :param raw_string: str, riga grezza di telemetria
    :return: tuple[int, float, str]
    """

    raw_string = raw_string.strip()  # Rimuove eventuali spazi bianchi all'inizio e alla fine della riga
    cutted_string = raw_string.split("|")  # Divide la riga in base al carattere "|"
    valori_estratti = []

    if len(cutted_string) != 3:
        raise ValueError("La riga di telemetria non è nel formato corretto.")

    for element in cutted_string:
        element = element.strip()  # Rimuove eventuali spazi bianchi all'inizio e alla fine di ogni elemento
        key_value = element.split(":",1) 
        valori_estratti.append(key_value[1].strip())



def test_parse_telemetria():
    casi_test = [
        # (input_raw, output_atteso)
        ("ID: 104 | TEMP: 37.2 | STATUS: ok ", (104, 37.2, "OK")),
        ("ID:88|TEMP:-4.5|STATUS:warning", (88, -4.5, "WARNING")),
        ("ID: 0 | TEMP: 0.0 | STATUS: error", (0, 0.0, "ERROR")),
        ("ID:   12  | TEMP:  25.65  | STATUS:   STANDBY   ", (12, 25.65, "STANDBY")),
    ]

    for i, (riga, atteso) in enumerate(casi_test, 1):
        risultato = parse_telemetria(riga)
        assert risultato == atteso, f"Test {i} fallito: atteso {atteso}, ottenuto {risultato}"
        assert isinstance(risultato[0], int), f"Test {i}: ID non è int ({type(risultato[0])})"
        assert isinstance(risultato[1], float), f"Test {i}: TEMP non è float ({type(risultato[1])})"
        assert isinstance(risultato[2], str), f"Test {i}: STATUS non è str ({type(risultato[2])})"

    print("Tutti i test sono passati con successo.")

if __name__ == "__main__":
    test_parse_telemetria()



    