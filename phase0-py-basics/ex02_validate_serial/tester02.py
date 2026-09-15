from validate_serials import validate_serials

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