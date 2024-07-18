for lettera in "ciao":
    if lettera == "c":
        print("****")
        print("*   ")
        print("*   ")
        print("****", end="")
    else:
        print(lettera, end="")

print("\n-----")

testo = "ciao"
for indice in range(0, len(testo)):
    print("ciao"[indice], end="")
print("\n-----")

print("supercalifragilistichespiralidoso"[8:10])
testo = "supercalifragilistichespiralidoso"
print(testo[:5])
print(testo[5:10])
print(testo[3:-3])
