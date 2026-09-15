"""Entry point principale per l'esecuzione della pipeline su file di test.

Lancia la lettura del log, stampa le metriche grezze aggregate e salva
il report JSON formattato sul disco.
"""

from pathlib import Path
from pprint import pprint
from pipeline import export_session_reports, file_data_reading

if __name__ == "__main__":
    # Percorsi dei dati: input CSV e destinazione del report finale JSON
    raw_path = "/Users/MatteoBollini/Documents/Python-projects/phase0-py-basics/pj0/data/test_data.csv"
    raw_output_path = "/Users/MatteoBollini/Documents/Python-projects/phase0-py-basics/pj0/output/session_reports.json"

    file_path = Path(raw_path)
    output_path = Path(raw_output_path)

    # 1. Pipeline di lettura, filtraggio e aggregazione
    unfiltered_data = file_data_reading(file_path)

    print("\n--- STATO AGGREGATI IN MEMORIA ---")
    pprint(unfiltered_data)

    # 2. Esportazione persistente su JSON
    export_session_reports(unfiltered_data, output_path)
    print(f"\nReport esportato con successo in: {output_path.resolve()}")