'''
try:
    file = open(".\\9-exceptions-files\\miofile2.txt")
    """
    print(file.read())
    print(file.readline(), end="")
    print(file.readline(), end="")
    """
    for line in file:
        print(line, end="")
except IOError as ioerror:
    print("errore file")
finally:
    chiudi il file
'''

# questo chiama in automatico finally file.close()
try:
    with open(".\\9-exceptions-files\\miofile.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
except FileNotFoundError as error:
    print("file non trovato")