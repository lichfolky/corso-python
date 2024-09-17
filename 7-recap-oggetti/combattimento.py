class Combattimento:
    def __init__(self, pg, mostro):
        self.pg = pg
        self.mostro = mostro

    def combat(self):
        danni = self.pg.attacca()
        self.mostro.ferisci(danni)