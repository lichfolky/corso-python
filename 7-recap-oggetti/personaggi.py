import random 

class Personaggio:
    def __init__(self,pf,nome,des,str,int):
        self.pf = pf
        self.nome = nome
        self.des = des
        self.str = str
        self.int = int

    def attacca(self):
        return random.randint(1,6)
    
    def set_nome(self, nuovo_nome):
        self.nome = nuovo_nome 

class Ladro(Personaggio):
    def nasconditi(self):
        print("mi sono nascosto!")

    def scassina(self):
        print("ho scassinato la serrura!")

    def attacca(self):
        return super().attacca() + self.des

class Mago(Personaggio):
    def attacca(self):
        return super().attacca() + self.int
    
class Guerriero(Personaggio):
    def attacca(self):
        return super().attacca() + self.str