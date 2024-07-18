for riga in range(1, 11):
    for colonna in range(1, 11):
        print(riga * colonna, end=", ")
    print()

for step in range(1, 11):
    for i in range(0, 11 * step, step):
        print(i, end=", ")
    print()
