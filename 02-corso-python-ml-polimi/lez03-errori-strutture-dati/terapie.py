
# input
PRESCRITTE = {("Rossi", "antibiotico"),("Bianchi", "cortisone"), ("Verdi", "antibiotico")}
REGISTRO = [("Rossi", "antibiotico"),("Verdi", "cortisone"),("Rossi", "antibiotico")]

# inizializzazione
registro: set = set(REGISTRO)
mancanti: set = {}
senza_prescrizione: set = {}

# filtro

# elaborazione
mancanti = PRESCRITTE - registro
senza_prescrizione =  registro - PRESCRITTE

# output
print(mancanti)
print(senza_prescrizione)
