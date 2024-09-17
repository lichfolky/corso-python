class Mostro:
    is_vivo = True

    def __init__(self, input_nome, pf):
        self.nome = input_nome
        self.pf = pf

    def ruggisci(self):
        print("Grrr sono", self.nome, "PF: ", self.pf)

    def ferisci(self, danni):
        if self.is_vivo:
            print(self.nome, "subisce",danni,"danni")
            self.pf -= danni
            if self.pf <= 0:
                print(self.nome, "MORTO!")
                self.pf = 0
                self.is_vivo = False