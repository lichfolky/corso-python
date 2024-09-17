from mostro import Mostro
from personaggi import Ladro, Guerriero, Mago
from combattimento import Combattimento

mio_pg = Mago(10,"Beppe",5,2,2)
mio_mostro = Mostro("Goblin", 10)
mio_mostro2 = Mostro("Mummia", 22)

mio_mostro.ruggisci()
mio_mostro2.ruggisci()

cmb = Combattimento(mio_pg, mio_mostro)
cmb.combat()
cmb.combat()
 
print(mio_pg.attacca())