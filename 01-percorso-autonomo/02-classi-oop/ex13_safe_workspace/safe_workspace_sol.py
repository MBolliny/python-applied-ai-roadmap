from pathlib import Path
import shutil

# Import puntato al tuo file di lavoro:
from safe_workspace import SafeWorkspace

# Per verificare a specchio la soluzione di riferimento:
# from safe_workspace_sol import SafeWorkspace

print("--- AVVIO VERIFICA LINEARE EX31 (SafeWorkspace) ---")

cartella_test = Path("./tmp_test_workspace")
cartella_test.mkdir(exist_ok=True)

try:
    # -------------------------------------------------------------------------
    # TEST 1: Esecuzione nominale (La cartella deve sparire all'uscita)
    # -------------------------------------------------------------------------
    percorso_usato = None
    with SafeWorkspace(cartella_test, "lavoro_01") as area_lavoro:
        percorso_usato = area_lavoro
        file_dati = area_lavoro / "letture_grezze.dat"
        file_dati.write_text("sensore_temperatura=36.6")

        if percorso_usato.exists() and file_dati.exists():
            print(
                "[OK] Test 1: Cartella e file creati correttamente nel blocco with"
            )
        else:
            print("[FAIL] Test 1: Cartella o file non presenti durante il blocco")

    if not percorso_usato.exists():
        print("[OK] Test 1: Cartella ripulita con successo all'uscita del blocco")
    else:
        print("[FAIL] Test 1: La cartella è ancora presente sul disco")

    # -------------------------------------------------------------------------
    # TEST 2: Errore con archivio diagnostico attivo (archive_on_error=True)
    # -------------------------------------------------------------------------
    cartella_archiviata = cartella_test / "lavoro_02_failed"
    cartella_originale = cartella_test / "lavoro_02"

    try:
        with SafeWorkspace(
            cartella_test, "lavoro_02", archivia_su_errore=True
        ) as area_lavoro:
            (area_lavoro / "stato_parziale.log").write_text("crash_telemetria")
            raise ValueError("Errore simulato di acquisizione")
    except ValueError as err:
        print(f"[OK] Test 2: Eccezione intercettata all'esterno ({err})")

    if not cartella_originale.exists():
        print("[OK] Test 2: Cartella originale rimossa/rinominata")
    else:
        print("[FAIL] Test 2: La cartella originale esiste ancora")

    if cartella_archiviata.exists() and (
        cartella_archiviata / "stato_parziale.log"
    ).exists():
        print(
            "[OK] Test 2: Cartella archiviata con suffisso '_failed' e dati intatti"
        )
    else:
        print("[FAIL] Test 2: Cartella diagnostica non trovata o vuota")

    # -------------------------------------------------------------------------
    # TEST 3: Errore SENZA archivio diagnostico (archive_on_error=False)
    # -------------------------------------------------------------------------
    cartella_lavoro_03 = cartella_test / "lavoro_03"
    try:
        with SafeWorkspace(
            cartella_test, "lavoro_03", archivia_su_errore=False
        ) as area_lavoro:
            (area_lavoro / "scarto.tmp").write_text("dati_inutili")
            raise RuntimeError("Altro errore simulato")
    except RuntimeError:
        pass

    if not cartella_lavoro_03.exists():
        print(
            "[OK] Test 3: Cartella ripulita anche dopo crash se archive_on_error=False"
        )
    else:
        print("[FAIL] Test 3: La cartella non è stata cancellata dopo il crash")

finally:
    # Pulizia totale dell'area test
    if cartella_test.exists():
        shutil.rmtree(cartella_test)
    print("--- VERIFICA COMPLETATA ---")