from datetime import datetime
class Todo:
    is_completato = False

    # descrizione parametro di default
    def __init__(self, nome, ora_inizio, ora_fine, luogo, descrizione=""):
        self.nome = nome
        self.ora_inizio = ora_inizio
        self.ora_fine = ora_fine
        self.luogo = luogo
        self.descrizione = descrizione

    def completa(self):
        self.is_completato = True

    def __str__(self):
        return "("+ self.nome + " at " + self.ora_inizio.strftime("%H:%M") + ")"