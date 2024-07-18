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

parole = ["Hello", "World", "in", "a", "frame"]
print("\033[38;5;20m"+ 9*"*".center(100))
for parola in parole:
    print("*", parola + " " * (5-len(parola)), "*")
print(9*"*"+"\033[0m".center(100))