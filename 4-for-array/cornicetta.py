## Dato l'array ["Hello", "World","in" ,"a","frame"] creare:
"""
*********
* Hello *
* World *
* in    *
* a     *
* frame *
*********
"""

VIOLETTO ="\033[38;5;20m"
END_COLORE = "\033[0m"

parole = ["All", "work", "and", "no", "play", "makes", "Folcarelli", "a", "dull", "boy"]

## trova parola più lunga
max_len = 0
for parola in parole:
    if len(parola) > max_len:
        max_len = len(parola)


print(VIOLETTO + (max_len + 4) * "*")

for parola in parole:
    print("* " + parola + " " * (max_len - len(parola)) + " *")
    
print(9*"*"+END_COLORE)