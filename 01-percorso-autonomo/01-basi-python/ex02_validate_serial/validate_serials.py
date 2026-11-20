def validate_serials(serial_list: list[str], numeric_only: bool) -> list[str]:
	# docstring
	''' docstring '''

	# inizializzo
	output_list: list[str] = []
	standard_len = 8

	for sample in serial_list:

		# verifico dati
		prefix = sample[:4]
		code = sample[4:]

		if len(sample) != standard_len or prefix != "SMP-" or not code.isdigit():
			continue

		payload = code if numeric_only else sample
		output_list.append(payload)
			
	return output_list


