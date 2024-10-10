'''
Ottieni il messaggio in codice nel file di testo "messaggio.txt" 
La frase segreta è composta dall'iniziale della 2a parola di ogni riga
(attenzione ai simboli)
'''
import re  

class MioError(Exception):
    pass

messaggioSegreto = ""
try:
    with open("9-exceptions-files\\messaggio.txt", "r", encoding="utf-8") as file:
        # print(file.read())
        for line in file:
            # print(line, end="")
            line = line.lower()
            line = re.sub(r'[^\w]', ' ', line)
            # per ogni parola prendo la prima lettera di ogni seconda parola 
            messaggioSegreto += line.split()[1][0]
    print(messaggioSegreto)
    # raise MioError("ciao questo è un mio errore")
except FileNotFoundError as error:
    print("file non trovato")


