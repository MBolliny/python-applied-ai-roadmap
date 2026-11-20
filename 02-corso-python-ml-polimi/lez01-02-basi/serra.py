import sys

# inizializzazione
# misurazioni = [45, 38, 72, 30]
misurazioni = []

count_secco = 0
count_letture_valide = 0

sum_misure_valide = 0

smetti_lettura = 0
j = 1

# ?? servono tutte ste inizializzazioni in py?

SECCO = 40
GUASTO = 95

# conversione
for i in range(1, len(sys.argv)):
	misurazioni.append(int(sys.argv[i]))
print(misurazioni)

for misura in misurazioni:

	status = "OK"

	if misura < SECCO:
		status = "SECCO"
		count_secco += 1
		# uscita

	if misura > GUASTO:
		status = "GUASTO"

	# stampa
	print(f"t{j} - status: {status}")
	j += 1

	if status == "GUASTO":
		break

	# aggiornamento valori misure
	if status == "OK":
		sum_misure_valide += misura
		count_letture_valide += 1

# calcolo media
media_misure = float(sum_misure_valide) / count_letture_valide

# stampe finali
print(f"quante ore e' stato secco? {count_secco}")
print(f"media misure {media_misure}")

