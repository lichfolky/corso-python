from Strategy import Coda,Pila

class SuperTicket(Coda):
    
    def __init__(self, array = [], num_iniziale=0):
        super().__init__(array)
        # self.coda = array
        self.num_iniziale = num_iniziale
        self.num_ticket = num_iniziale

    # inserisci in coda
    def enqueue(self):
        super().enqueue(self.num_ticket)
        # self.queue.append(self.num_ticket)
        self.num_ticket += 1

    def numero_display(self):
        return self.queue[0]
    
# coda = ["😊", "😒", "😁", "😘"]
# nuovo_arrivato = "💀"

mia_coda = SuperTicket([],0)
mia_coda.enqueue()
mia_coda.enqueue()
mia_coda.enqueue()
mia_coda.enqueue()
print(mia_coda.queue)
print(mia_coda.dequeue())
print(mia_coda.queue)
print(mia_coda.numero_display())

