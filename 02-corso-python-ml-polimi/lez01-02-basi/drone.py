import sys
# verifica di ingresso
if len(sys.argv) <= 3:
	print("selezionare un numero maggore di whaypostn")
	sys.exit()

# verifica dopo
volo_consentito = True

if int(sys.argv[1]) < 30:
	print("carica batteria non sufficiente")
	volo_consentito = False

if float(sys.argv[2]) < 120:
	volo_consentito = False

if sys.argv[3] == "no":
	print("non e' stato inserito il gps")
	volo_consentito = False

if sys.argv[-1] == "base": 
	print("stazione finale non puo essere la base")
	volo_consentito = False

for element in sys.argv:
	if element == "zona_rossa":
		print("stazione zona rossa rilevata")
		volo_consentito = False

# condizione di uscita
if volo_consentito == False:
	print("volo non consentito - mancaza di requisiti")
else:
	print("volo consentito - requisiti rispettati")

# ?? - co