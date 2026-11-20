def parse_can_telemetry(
    frames: list[str], as_celsius: bool = False
) -> list[tuple[str, int] | float]:
    """Parses a list of CAN telemetry frames and extracts temperature data."""
    print("frames in ingresso: \n", frames)

    # 1. Assegnazione dell'oggetto lista vuota (non solo type hint)
    output: list[tuple[str, int] | float] = []

    for sample in frames:
        # verifica STRINGA
        if not sample:
            print("stringa vuota, passo al prossimo campione")
            continue

        # Pulizia e Divisione
        cleaned_sample = sample.strip()
        token_list = cleaned_sample.split(":")

        # verifica LISTA in uscita
        if len(token_list) != 3:
            print("stringa non corretta, passo al prossimo campione")
            continue

        # Validazioni di specifica CAN
        if token_list[0] != "TEMP":
            continue
        if len(token_list[1]) != 2 or not token_list[1].isdigit():
            continue
        if len(token_list[2]) != 5:
            continue

        # sistemo i dati da elaborare
        try:
            temperature = int(token_list[2])
        except ValueError:
            print("cast temperatura str->int fallito")
            continue

        # elaborazione
        if not as_celsius:
            output.append((token_list[1], temperature))
        else:
            # 2. Usa l'intero già convertito per la divisione aritmetica
            temperature_c = temperature / 1000.0
            output.append(temperature_c)

    return output