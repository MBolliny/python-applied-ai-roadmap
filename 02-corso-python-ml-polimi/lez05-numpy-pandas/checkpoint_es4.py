'''Esercizietto prima di P0-es4
Situazione: un laboratorio ha fatto 10 test. L'esito di ciascuno è 0 (negativo) o 1 (positivo) e arriva in un array di forma (10, 1):
esiti = [[0], [1], [1], [0], [1], [1], [1], [0], [1], [1]]
Obiettivo: portare gli esiti a forma (10,), contare quanti sono negativi e quanti positivi, e calcolare la frazione di positivi.
Vincoli: nessun ciclo for; usa solo quello che hai studiato nei gruppi 2 e 4. Dove: mini_conteggio.py nella cartella lez05-numpy-pandas, 5-10 righe.
Come verifichi: la forma stampata è (10,), i negativi sono 3, i pos'''
import numpy as np

# converto da lista -> array
esiti = [[0], [1], [1], [0], [1], [1], [1], [0], [1], [1]]
arr_esiti = np.array(esiti)

# cambia la forma dell'array
arr_esiti_res = arr_esiti.reshape(10,)

# cacola e stampa valori == 1 mettendoli in un altro array
positive = arr_esiti_res[arr_esiti_res == 1]
negative = arr_esiti_res.size - positive.size
print(positive.size)
print(negative)

print(positive.size / arr_esiti_res.size)
