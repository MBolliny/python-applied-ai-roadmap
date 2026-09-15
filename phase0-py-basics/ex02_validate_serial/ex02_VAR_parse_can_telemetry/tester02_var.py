"""
tester_ex02.py - Minimal verification suite.
"""

from ex02_VAR_parse_can_telemetry import parse_can_telemetry

def main() -> None:
    # Test 1: as_celsius = False (Nominale + Rumore/Formati non conformi)
    frames_raw = [
        "TEMP:01:37200",
        "PRESS:01:01013",
        "TEMP:02:36850",
        "TEMP:3:37000",
        "TEMP:04:37A00",
        "",
        "TEMP:05:12345:EXTRA",
        "TEMP:06:1234",
    ]
    expected_raw = [("01", 37200), ("02", 36850)]
    result_raw = parse_can_telemetry(frames_raw, as_celsius=False)

    if result_raw == expected_raw:
        print("[OK] Test 1 (Raw Tuples)")
    else:
        print(f"[FAIL] Test 1 - Atteso: {expected_raw} | Ottenuto: {result_raw}")

    # Test 2: as_celsius = True (Conversione in Celsius)
    frames_celsius = [
        "TEMP:01:37200",
        "NOISE",
        "TEMP:99:41000",
        "TEMP:02:invalid",
        "TEMP:03:36500",
    ]
    expected_celsius = [37.2, 41.0, 36.5]
    result_celsius = parse_can_telemetry(frames_celsius, as_celsius=True)

    if result_celsius == expected_celsius:
        print("[OK] Test 2 (Celsius Float)")
    else:
        print(f"[FAIL] Test 2 - Atteso: {expected_celsius} | Ottenuto: {result_celsius}")


if __name__ == "__main__":
    main()