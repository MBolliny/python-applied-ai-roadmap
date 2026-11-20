def analyze_cohorts(group_a: list[str], group_b: list[str]) -> dict[str, set[str]]:
    
    # Se un parametro è None, interrompe subito l'esecuzione
    if group_a is None or group_b is None:
        raise ValueError("group_a e group_b non possono essere None.")

    # Se i dati sono validi, converte e restituisce
    set_a: set[str] = set(group_a)
    set_b: set[str] = set(group_b)

    return {
        "common": set_a & set_b,
        "exclusive": set_a ^ set_b,
        "total": set_a | set_b,
    }

def telemetric(patient_list: dict[str, list[float]], threshold: int = 15, window: int = 3) -> list[str]
    #docstirng

    # inizializzazione 
    above_threshold_patients: list[str] = []
    
    # Iterazione su chiave (ID) e valore (buffer serie temporale)
        for patient_id, readings in patient_telemetry.items():
            # Estrazione degli ultimi N campioni (safe slicing)
            recent_window = readings[-window_size:]

            # Calcolo media su campioni validi per evitare ZeroDivisionError
            if recent_window:
                rolling_mean = sum(recent_window) / len(recent_window)

                # Inclusione solo dei pazienti che superano strettamente la soglia
                if rolling_mean > threshold:
                    above_threshold_patients.append(patient_id)

return above_threshold_pat[]
