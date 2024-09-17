from macchinetta import Macchinetta
macchina = Macchinetta()
macchina.print_menu()
# Questo stampa il valore di default del product B11
# print(macchina.menu["B11"].codice)
macchina.insert_coins(1)

try:
    resto = macchina.buy_product("Bciao")
    print(resto)
except KeyError as keyError:
    print("ERRORE - codice sbagliato")
except Exception as error:
    print("ERRORE", error)
