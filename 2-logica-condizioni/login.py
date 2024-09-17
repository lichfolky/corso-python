user = "Beppe"
password = "12345"

user_inserita = input("inserisci l'utente\n")

if user_inserita == user:
    password_inserita = input("inserisci la password\n")
    if password_inserita == password:
        print("Access granted :)")
    else:
        print("ACCESS DENIED!")
