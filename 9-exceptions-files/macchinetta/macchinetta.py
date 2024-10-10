class Product:
    # costruttore
    def __init__(self, nome, prezzo, codice="NoCode"):
        self.nome = nome
        self.prezzo = prezzo
        self.codice = codice

    def __str__(self):
        return self.codice + "-" + self.nome + ": " + str(self.prezzo)

class Macchinetta:

    credit = 0
    menu = {
        "B15": Product("caffè", 0.55, "B15"),
        "B11": Product("latte", 0.45),
        "B10": Product("macchiato", 0.55, "B10"),
    }

    '''
    menu_array = [["caffè", 0.55], ["latte", 0.45], ["macchiato", 0.55]]

    menu_dizionario = {
        "B15": ["caffè", 0.55],
        "B11": ["latte", 0.45],
        "B10": ["macchiato", 0.55],
    }

    menu_dizionario_dizionario = {
        "B15": {"nome":"caffè","prezzo": 0.55},
        "B11": {"nome":"latte","prezzo": 0.45},
        "B10": {"nome":"macchiatp","prezzo": 0.55},
    }

    menu = {
        "B15": Product("caffè", 0.55, "B15"),
        "B11": Product("latte", 0.45, "B11"),
        "B10": Product("macchiatp", 0.55, "B10"),
    }

    # prezzi del macchiato
    menu[2][1]
    menu_dizionario["B10"][1]
    menu_dizionario_dizionario["B10"]["prezzo"]
    menu["B10"].prezzo
    '''
 

    def insert_coins(self, coins):
        self.credit += coins

    def print_menu(self):
        print("---")
        print("MENU!")
        for codice in self.menu:
            print(self.menu[codice])
        print("---")

    def buy_product(self, codice):

        # ottengo il prezzo del prodotto rappresentato da codice
        prodotto = self.menu[codice]
        prezzo_del_prodotto = prodotto.prezzo

        if prezzo_del_prodotto > self.credit:
            raise Exception("NO ENOUGHT MONEY")

        # versione compatta:
        # prezzo = self.menu[codice].prezzo

        # ottengo il resto rimanente dopo l'acquisto
        resto = self.credit - prezzo_del_prodotto
        resto = round(resto, 2)

        # imposto il credito a 0
        self.credit = 0
        # restituisco il resto
        return resto