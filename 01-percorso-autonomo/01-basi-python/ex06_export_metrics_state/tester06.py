import json
import shutil
from pathlib import Path
from export_metrics_state_sol import export_metrics_state


def main() -> None:
    test_dir = Path("temp_test_output")
    test_dir.mkdir(exist_ok=True)

    test_cases = [
        {
            "name": "Standard telemetry with float rounding",
            "metrics": {
                "sensor_id": "TEMP_01",
                "avg_temp": 37.1567,
                "max_temp": 38.0012,
            },
            "path": test_dir / "state.json",
            "round_digits": 2,
            "expected_payload": {
                "sensor_id": "TEMP_01",
                "avg_temp": 37.16,
                "max_temp": 38.0,
            },
        },
        {
            "name": "Empty dictionary triggers IDLE payload",
            "metrics": {},
            "path": test_dir / "state_empty.json",
            "round_digits": 2,
            "expected_payload": {"status": "IDLE", "metrics": {}},
        },
        {
            "name": "Nested non-existent directory auto-creation",
            "metrics": {"cal_factor": 1.99876},
            "path": test_dir / "nested" / "logs" / "deep_state.json",
            "round_digits": 3,
            "expected_payload": {"cal_factor": 1.999},
        },
    ]

    all_passed = True

    try:
        for idx, tc in enumerate(test_cases, 1):
            success = export_metrics_state(
                tc["metrics"], tc["path"], tc["round_digits"]
            )
            if not success or not tc["path"].exists():
                print(f"[FAIL] Test {idx} ({tc['name']}): Export failed or file missing.")
                all_passed = False
                continue

            with open(tc["path"], "r", encoding="utf-8") as f:
                saved_data = json.load(f)

            if saved_data == tc["expected_payload"]:
                print(f"[OK] Test {idx}: {tc['name']}")
            else:
                print(
                    f"[FAIL] Test {idx} ({tc['name']}): Payload mismatch.\n"
                    f"  Expected: {tc['expected_payload']}\n"
                    f"  Got:      {saved_data}"
                )
                all_passed = False

    finally:
        # Cleanup delle risorse temporanee di test
        if test_dir.exists():
            shutil.rmtree(test_dir)

    print("\n" + ("=" * 40))
    print("RESULT:", "ALL TESTS PASSED" if all_passed else "SOME TESTS FAILED")
    print("=" * 40)


if __name__ == "__main__":
    main()