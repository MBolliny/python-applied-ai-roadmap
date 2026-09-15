def analizza_coorti(
		gruppo_a: list[str], 
		gruppo_b: list[str], 
		telemetria: dict[str, list[float]], 
		soglia: float,
		) -> dict[str, set[str] | list[str]]:

	# documentazione
	
	# inizializzazione
	wind_size = 3
	output_dict = dict[str, set[str] | list[str]] = {}
	output_telemtry_list: list[str] = []

	try: 
		set_a = set(gruppo_a)
		set_b  = set(gruppo_b)
	except:
		print("errore nella conversione")
		return {}

	# elaborazione set
	output_dict = {
			"comuni": set_a & set_b,
			"esclusivi": set_a ^ set_b,
			"totali": set_a | set_b
					}

	if not telemetria:
		return output_dict		

	# calcolo MEDIA
	for id, telemetry_list in telemetria.item():
		sum = 0

		# verifico condizioni
		if telemetry_list < wind_size:
			print("lista troppo corta, passo al prossimo cammpione")
			continue
			
		# calcolo e conversione
		for i in range(1,wind_size):
			sum += telemetry_list[-i]

		try:
			media = float(sum / wind_size)
		except:
			print("errore nella conversione nel calcolo media")
			continue

		# verifica
		if media > soglia:
			output_telemtry_list.append(id)

	return (output_dict, output_telemtry_list)




