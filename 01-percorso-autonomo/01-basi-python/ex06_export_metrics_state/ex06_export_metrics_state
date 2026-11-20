import json
from pathlib import Path
from typing import Any


def export_metrics_state(
    metrics_data: dict[str, float | str],
    file_path: str | Path,
    round_digits: int = 2,
) -> bool:
    """Serialize system metrics to a JSON configuration file with rounded floats.

    Args:
        metrics_data: Telemetry dictionary mapping keys to float or str values.
        file_path: Target filesystem destination as string or Path object.
        round_digits: Decimal precision to apply to float values.

    Returns:
        True if the file was written successfully, False otherwise.
    """
    target_path = Path(file_path)

    # Gestione esplicita dello stato IDLE su input vuoto
    if not metrics_data:
        payload: dict[str, Any] = {"status": "IDLE", "metrics": {}}
    else:
        # Trasformazione pura: round selettivo solo su tipi float numerici
        payload = {
            key: round(value, round_digits) if isinstance(value, float) else value
            for key, value in metrics_data.items()
        }

    try:
        # Assicura la presenza dell'albero delle cartelle padre
        target_path.parent.mkdir(parents=True, exist_ok=True)

        with target_path.open("w", encoding="utf-8") as json_file:
            json.dump(payload, json_file, indent=2, ensure_ascii=False)
        return True

    except (OSError, TypeError) as err:
        # In produzione si userebbe un logger configurato: logger.error(...)
        return False