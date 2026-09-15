from pathlib import Path


def ingest_telemetry_stream(file_path: str | Path) -> list[dict[str, int | float]]:
    # verifico
    path = Path(file_path)
    
    # inizializzo
    output_list: list[dict[str, int | float]] = []

    # elaboro
 
   	# provo ad aprire il file
    try:
    	with open(path, mode = "r", endoing = "utf-8") as file 
    		for raw_line in file:
	    		# pulisco al stringa per lavorari
	    		cleaned_line = line.strip()

	    		# verifico la stringa
	    		if not cleaned_line:
	    			return []

	    		# estrggo valori
	    		parts = cleaned_line.split(",")

	    		# verifico che siano ok
	    		# 1. lista -> lunghezza
	    		if len(parts) != 3
	    			continue

	    		try:
				    ts = int(parts[0])
				    temp = float(parts[1])
				    press = float(parts[2])
				except ValueError:
				    continue  # Intercetta token corrotti come "CORRUPT", "N/A", "null" o formati non validi
	except (FileNotFoundError, OSError):
	        # File non trovato o errore di basso livello (es. permessi mancanti)
	        return []

    return output_list