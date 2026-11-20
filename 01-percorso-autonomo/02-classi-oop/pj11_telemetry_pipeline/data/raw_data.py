def genera_flusso_telemetria_simulato():
    """Genera una sequenza fittizia di pacchetti telemetrici grezzi.

    Include letture fisiologiche corrette, violazioni di soglia, anomalie di
    tipo e canali non censiti per testare i controlli.
    """
    flusso_dati = [
        # --- BLOCCO 1: Dati nominali e validi ---
        ("BPM", 72.0),
        ("SPO2", 98.5),
        ("PA_SISTOLICA", 120.0),
        ("BPM", 75.0),
        ("SPO2", 99.0),
        # --- BLOCCO 2: Canali non configurati nel monitor ---
        ("TEMPERATURA", 36.8),
        ("GLICEMIA", 110.0),
        # --- BLOCCO 3: Valori fuori dal range fisico del sensore ---
        ("BPM", 280.0),  # Troppo alto (tachicardia estrema o rumore)
        ("SPO2", 105.0),  # Fisicamente impossibile (> 100%)
        ("PA_SISTOLICA", 30.0),  # Sotto il limite minimo strumentale
        # --- BLOCCO 4: Errori di tipo (dati corrotti dalla linea) ---
        ("BPM", "OFFLINE"),  # Stringa al posto di un float
        ("SPO2", True),  # Booleano (sottotipo di int in Python)
        ("PA_SISTOLICA", None),  # Lettura nulla
        # --- BLOCCO 5: Ripresa flusso valido ---
        ("BPM", 78.0),
        ("SPO2", 97.0),
        ("PA_SISTOLICA", 118.0),
    ]

    return flusso_dati
