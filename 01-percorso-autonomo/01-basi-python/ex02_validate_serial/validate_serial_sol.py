def validate_serials(
    serial_list: list[str], numeric_only: bool = False
) -> list[str]:
    """Filters and sanitizes biological specimen serial identifiers.

    Validation rules:
    - Total length must be exactly 8 characters.
    - Prefix must match 'SMP-'.
    - Suffix must contain 4 numerical digits.
    """
    valid_serials: list[str] = []
    required_length: int = 8

    for serial in serial_list:
        # 1. Estrazione porzioni tramite slicing O(1)
        prefix = serial[:4]
        numeric_code = serial[4:]

        # 2. Guard Clause: Rifiuto anticipato se non rispetta le specifiche
        if (
            len(serial) != required_length
            or prefix != "SMP-"
            or not numeric_code.isdigit()
        ):
            continue

        # 3. Emissione payload in base al flag
        payload = numeric_code if numeric_only else serial
        valid_serials.append(payload)

    return valid_serials


# =====================================================================
# TEST RUNNER
# =====================================================================
if __name__ == "__main__":
    test_batch = [
        "SMP-1042",  # Valido
        "SMP-99",  # Corto (< 8)
        "ERR-4040",  # Prefisso errato
        "SMP-8831",  # Valido
        "SMP-ABCD",  # Lettere al posto di cifre
        "SMP-10429",  # Lungo (> 8)
        "",  # Stringa vuota
    ]

    # Test 1: Mantenimento codice intero
    res_full = validate_serials(test_batch, numeric_only=False)
    assert res_full == ["SMP-1042", "SMP-8831"], f"Fallito Full: {res_full}"

    # Test 2: Estrazione sole cifre numeriche
    res_num = validate_serials(test_batch, numeric_only=True)
    assert res_num == ["1042", "8831"], f"Fallito Numeric: {res_num}"

    # Test 3: Lista vuota
    assert validate_serials([], numeric_only=False) == []

    print("[ALL TESTS PASSED]: Validazione e filtraggio seriali conformi.")