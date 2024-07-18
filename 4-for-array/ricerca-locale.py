nomi = ["ezio", "beppe", "ayeye", "maria", "marco", "emilia", "anna"]

for i in range(0, len(nomi)):
    if nomi[i] == "maria":
        print("TROVATO", nomi[i], "all'indice", i)
        break
    print(i)
