num = int(input("num:\n"))

# metodo 1
print("1" * num)

# metodo 2
i = 0
while i < num:
    print("1", end="")
    i += 1
print()

# metodo 3
i = 0
unario = ""
while i < num:
    unario += "1"
    i += 1
print(unario)
