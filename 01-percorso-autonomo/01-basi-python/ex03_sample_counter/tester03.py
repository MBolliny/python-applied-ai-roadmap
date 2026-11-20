from sample_counter import sample_counter

if __name__ == "__main__":
   # 1. Caso nominale: conteggio assoluto
       samples_a = ["siero", "PLASMA", "SIERO", "SANGUE", "SIERO"]
       res_a = sample_counter(samples_a, normalize=False)
       print("Input:", samples_a)
       print("Conteggio Assoluto:", res_a)
       print("-" * 40)
   
       # 2. Caso con normalizzazione
       samples_b = ["PLASMA", "siero", "PLASMA", "PLASMA"]
       res_b = sample_counter(samples_b, normalize=True)
       print("Input:", samples_b)
       print("Frequenze Relative:", res_b)
       print("-" * 40)
   
       # 3. Edge case: lista vuota
       samples_c: list[str] = []
       res_c = sample_counter(samples_c, normalize=True)
       print("Input:", samples_c)
       print("Lista Vuota (normalize =True):", res_c)
   