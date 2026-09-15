def count_samples(readings: list[str], normalize: bool = False) -> dict[str, float]:
    """
    Conta le frequenze assolute o normalizzate dei campioni biologici in ingresso.
    """
    # Step 1: Guard Clause - Verifica input vuoto per prevenire ZeroDivisionError
    if not readings:
        return {}

    counts: dict[str, int] = {}

    # Step 2: Accumulo frequenze assolute con fallback a 0 per nuove categorie
    for sample in readings:
        counts[sample] = counts.get(sample, 0) + 1

    # Step 3: Trasformazione output - Conteggio assoluto (cast a float)
    if not normalize:
        return {sample: float(count) for sample, count in counts.items()}

    # Step 4: Trasformazione output - Normalizzazione relativa sul totale campioni
    total_samples = len(readings)
    return {sample: count / total_samples for sample, count in counts.items()}