from pathlib import Path


def ingest_telemetry_stream(file_path: str | Path) -> list[dict[str, int | float]]:
    """Parse a CSV telemetry stream file and return valid data records.

    Corrupted rows (e.g. invalid fields, failed casts) are skipped.
    If the file does not exist, an empty list is returned.

    :param file_path: Path to the telemetry CSV file.
    :return: List of telemetry dictionaries with 'ts', 'temp', and 'press' keys.
    """
    path = Path(file_path)
    records: list[dict[str, int | float]] = []

    try:
        with open(path, mode="r", encoding="utf-8") as file:
            for raw_line in file:
                line = raw_line.strip()
                if not line:
                    continue  # Salta righe vuote prima del parsing

                parts = line.split(",")
                if len(parts) != 3:
                    continue  # Scarta record con cardinalità errata

                try:
                    records.append({
                        "ts": int(parts[0]),
                        "temp": float(parts[1]),
                        "press": float(parts[2]),
                    })
                except ValueError:
                    # Scarta token non convertibili (stringhe corrotte, nulli)
                    continue

    except (FileNotFoundError, OSError):
        # File non trovato o errore di basso livello (es. permessi mancanti)
        return []

    return records