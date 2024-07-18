import random
conteggi = []

numero_classi = 10
for i in range(0,numero_classi):
    conteggi.append(0)
    
print(conteggi)



# serie di dati temporali
temperature = []
 
for i in range(0,10):
    temperature.append(random.randint(-15,40))
    
print(temperature)


numeri = []
 
for i in range(0,10):
    numeri.append(i)
    
print(numeri)


list = list(range(0,5)) 
random.shuffle(list)
print(list)