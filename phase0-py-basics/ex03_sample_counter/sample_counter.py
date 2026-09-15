def sample_counter(sample_list: list[str], normalize: bool) -> dict[str, float]:

	# docstring

	# inizilizzo
	output_dict: dict[str, float] = {}

	# verifica 1
	if not sample_list:
		return {}

	# Verifica 2
	for sample in sample_list:
		filtered_sample = sample.upper()

		# elaboro
		output_dict[filtered_sample] = output_dict.get(filtered_sample, 0) + 1

	# casp limite
	if normalize:
		tot_sample = len(sample_list)
		for (key,value) in output_dict.items():
			output_dict[key] = value / tot_sample

	return output_dict
