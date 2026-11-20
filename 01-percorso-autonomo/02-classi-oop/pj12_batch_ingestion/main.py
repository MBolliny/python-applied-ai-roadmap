import json
from pathlib import Path
from src.lettura import CSVRecordParser, KeyValueRecordParser

class CorruptedPayloadError(Exception):
    """Sollevata quando un file è vuoto o corrotto."""
    pass

# Centralino di smistamento
PARSER_REGISTRY = {
    ".csv": CSVRecordParser,
    ".kv": KeyValueRecordParser,
}

def valida_e_filtra(cartella: Path) -> list[Path]:
    """Dogana: filtra spazzatura, controlla dimensione ed estensione."""
    file_validati = []
    for f in cartella.iterdir():
        if not f.is_file():
            continue
        # Salta file nascosti di sistema
        if f.name.startswith("."):
            continue

        # Controllo file vuoto
        if f.stat().st_size == 0:
            raise CorruptedPayloadError(f"File vuoto rilevato: {f.name}")

        # Controllo estensione supportata
        if f.suffix.lower() not in PARSER_REGISTRY:
            print(f"[DOGANA] Scartato formato non gestito: {f.name}")
            continue

        file_validati.append(f)
    return file_validati

def main():
    radice = Path(__file__).resolve().parent
    cartella_in = radice / "data" / "input"
    cartella_out = radice / "data" / "output"
    cartella_out.mkdir(parents=True, exist_ok=True)
    file_out = cartella_out / "dataset_standardizzato.json"

    # 1. Dogana
    file_pronti = valida_e_filtra(cartella_in)
    print(f"-> File approvati: {[f.name for f in file_pronti]}")

    # 2. Multiplexer ed estrazione
    dataset_completo = []
    for f in file_pronti:
        classe_parser = PARSER_REGISTRY[f.suffix.lower()]
        parser = classe_parser()
        record_estratti = parser.parse(f)
        dataset_completo.extend(record_estratti)
        print(f"-> Estratti {len(record_estratti)} record da {f.name}")

    # 3. Scrittura output
    with file_out.open("w", encoding="utf-8") as out:
        json.dump(dataset_completo, out, indent=2)

    print(f"[COMPLETATO] Salvati {len(dataset_completo)} record in {file_out.name}")


if __name__ == "__main__":
    main()
