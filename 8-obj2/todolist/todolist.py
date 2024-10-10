class TodoList:
    list = []

    def __init__(self, nome):
        self.nome = nome

    def add_todo(self, todo):
        self.list.append(todo)

    # Override di un metodo str
    def __str__(self):
        stringa_eventi = ""
        for evento in self.list:
            stringa_eventi += str(evento)
            if evento.is_completato:
                stringa_eventi +=  "-COMPLETATO-"
            stringa_eventi +=  ", "
        return self.nome + ": " + stringa_eventi

    def trova_e_completa(self, nome):
        for evento in self.list:
            if evento.nome == nome:
                evento.completa()
