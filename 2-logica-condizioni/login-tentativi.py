user_upper = "Beppe"
user_lower = "beppe"

password = "12345"
tentativi = 3
accesso_eseguito = False

user_inserita = input("inserisci l'utente\n")
if user_inserita == user_lower or user_inserita == user_upper:
    password_inserita = input("inserisci la password\n")
    if password_inserita == password:
        accesso_eseguito = True
        print("Access granted :)")
    else:
        tentativi = tentativi - 1
        print("ACCESS DENIED! Tentativi rimasti:", tentativi)
else:
    tentativi = tentativi - 1
    print("Utente non riconosciuto! Tentativi rimasti:", tentativi)

## TENTATIVO 2
if not accesso_eseguito:
    user_inserita = input("inserisci l'utente\n")
    if user_inserita == user_lower or user_inserita == user_upper:
        password_inserita = input("inserisci la password\n")
        if password_inserita == password:
            accesso_eseguito = True
            print("Access granted :)")
        else:
            tentativi = tentativi - 1
            print("ACCESS DENIED! Tentativi rimasti:", tentativi)
    else:
        tentativi = tentativi - 1
        print("Utente non riconosciuto! Tentativi rimasti:", tentativi)

## TENTATIVO 3
if not accesso_eseguito:
    user_inserita = input("inserisci l'utente\n")
    if user_inserita == user_lower or user_inserita == user_upper:
        password_inserita = input("inserisci la password\n")
        if password_inserita == password:
            accesso_eseguito = True
            print("Access granted :)")
        else:
            tentativi = tentativi - 1
            print("ACCESS DENIED! Tentativi rimasti:", tentativi)
    else:
        tentativi = tentativi - 1
        print("Utente non riconosciuto! Tentativi rimasti:", tentativi)
