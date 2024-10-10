class Coda:
    __num_segreto = 420

    def __init__(self, array = []):
        self.queue = array

    # inserisci in coda
    def enqueue(self, elemento):
        self.queue.append(elemento)

    # servi primo della coda
    def dequeue(self):
        return self.queue.pop(0)
    
class Pila:

    def __init__(self, array = []):
        self.stack = array

    # inserisci in coda
    def push(self, elemento):
        self.stack.append(elemento)

    # servi primo della coda
    def pop(self):
        return self.stack.pop()