"""
tester_ex03_v1.py - Minimal test suite for actuator duty tally.
"""

from ex03_VAR_tally_actuator_duty import tally_actuator_duty


def main() -> None:
    # Test 1: Absolute counts with default ignore_token ("IDLE")
    states_1 = ["PUMP_A", "IDLE", "HEATER_ON", "PUMP_A", "IDLE", "PUMP_A"]
    expected_1 = {"PUMP_A": 3.0, "HEATER_ON": 1.0}
    result_1 = tally_actuator_duty(states_1, ignore_token="IDLE", relative_rate=False)

    # Cast manuale o confronto su float per uniformità contrattuale
    result_1_float = {k: float(v) for k, v in result_1.items()}
    if result_1_float == expected_1:
        print("[OK] Test 1 - Absolute Counts")
    else:
        print(f"[FAIL] Test 1 - Atteso: {expected_1} | Ottenuto: {result_1}")

    # Test 2: Normalized rate with custom sentinel ("NOOP")
    states_2 = ["VALVE_1", "NOOP", "VALVE_1", "VALVE_2", "NOOP"]
    expected_2 = {"VALVE_1": 2 / 3, "VALVE_2": 1 / 3}
    result_2 = tally_actuator_duty(states_2, ignore_token="NOOP", relative_rate=True)

    passed_2 = (
        len(result_2) == len(expected_2)
        and all(abs(result_2.get(k, 0.0) - v) < 1e-6 for k, v in expected_2.items())
    )
    if passed_2:
        print("[OK] Test 2 - Normalized Relative Rates")
    else:
        print(f"[FAIL] Test 2 - Atteso: {expected_2} | Ottenuto: {result_2}")

    # Test 3: Edge cases (Empty list and All Sentinel list -> Prevent division by zero)
    result_empty = tally_actuator_duty([],  ignore_token="IDLE", relative_rate=True)
    result_all_idle = tally_actuator_duty(["IDLE", "IDLE"], ignore_token="IDLE", relative_rate=True)

    if result_empty == {} and result_all_idle == {}:
        print("[OK] Test 3 - Edge Cases (Empty & All-Ignored)")
    else:
        print(f"[FAIL] Test 3 - Atteso: {{}} | Ottenuto: Empty={result_empty}, AllIdle={result_all_idle}")


if __name__ == "__main__":
    main()