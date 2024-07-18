password = "563"
password_trovata = False
password_generata = 0

# while password_generata < 1000:
while not password_trovata:

    # genero password numerica e la trasformo in stringa

    password_text = str(password_generata)
    password_text = (3 - len(password_text)) * "0" + password_text

    if password_text == password:
        print(password_text, ": ACCESS GRANTED!")
        password_trovata = True
    else:
        print(password_text, ": ACCESS DENIED!")
    password_generata += 1
