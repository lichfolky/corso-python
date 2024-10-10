import json


class Gatto:
    def __init__(self, nome, colore, eta):
        self.nome = nome
        self.colore = colore
        self.eta = eta

class GattoEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__


mio_gatto = Gatto("Ernesto", "Rosso", 8)


## print(mio_gatto.__dict__)
file = open("11-strutture-dati-logging\\gatto.txt","r+")
print(json.dumps(mio_gatto, cls=GattoEncoder))
json.dump(mio_gatto, cls=GattoEncoder, fp=file)

json_read = "['gatto','rosso','ernesto']"
    
obj = json.loads(json_read)
# print(gatto.nome)

## TODO