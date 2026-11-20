def export_metrics_state(
    metrics_data: dict[str, float | str],
    file_path: str | Path,
    round_digits: int = 2,
) -> bool:

    # iniziaizzazone
    target_path = path(file_path)
    payload: dict[str, Any] = {}


    # preparo dati
    if not metrics_data:
        payload: dict[str, Any] = {"idle", "dict vuoto"}
    
    else:
        for key, value in metrics_data.items():
            if isinstance(value, float):
                # Se il valore è virgola, applica l'arrotondamento
                payload[key] = round(value, round_digits)
            else:
                # Se è una stringa o altro tipo, copialo intatto
                payload[key] = value


  
    try: 
        # verifica e creazione directory
        target_path.parent.mkdir(parent=True, exist_ok=True)

        # cerco di aprrie il file
        with open(file_path, mode="w", encoding="utf-8") as file
            json.dump(payload, file, indent=2)

        return True
    except: 
        return = False

