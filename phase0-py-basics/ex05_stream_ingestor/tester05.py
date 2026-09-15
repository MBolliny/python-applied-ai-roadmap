from pathlib import Path
from ingest_telemetry_stream_sol import ingest_telemetry_stream


def main() -> None:
    test_dir = Path("test_data_temp")
    test_dir.mkdir(exist_ok=True)
    
    valid_and_corrupt_file = test_dir / "telemetry_mixed.csv"
    valid_and_corrupt_file.write_text(
        "1700000000,37.2,101.3\n"
        "1700000010,CORRUPT,101.4\n"
        "1700000020,37.5\n"
        "1700000030,37.4,101.1\n"
        "\n"  # Riga vuota
        "1700000040,36.8,100.9,EXTRA_FIELD\n",
        encoding="utf-8"
    )

    empty_file = test_dir / "empty.csv"
    empty_file.write_text("", encoding="utf-8")
    
    non_existent_file = test_dir / "missing.csv"

    # Test Cases
    tests = [
        (
            "Nominale con record corrotti e spuri",
            valid_and_corrupt_file,
            [
                {"ts": 1700000000, "temp": 37.2, "press": 101.3},
                {"ts": 1700000030, "temp": 37.4, "press": 101.1},
            ],
        ),
        (
            "File vuoto",
            empty_file,
            [],
        ),
        (
            "File inesistente",
            non_existent_file,
            [],
        ),
    ]

    for label, path, expected in tests:
        actual = ingest_telemetry_stream(path)
        if actual == expected:
            print(f"[OK] {label}")
        else:
            print(f"[FAIL] {label}")
            print(f"   Atteso:  {expected}")
            print(f"   Ottenuto: {actual}")

    # Teardown
    for file in test_dir.iterdir():
        file.unlink()
    test_dir.rmdir()


if __name__ == "__main__":
    main()