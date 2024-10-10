import random

def scambia_due_elementi(bicchieri):
    el1 = random.randint(0, len(bicchieri)- 1)
    el2 = random.randint(0, len(bicchieri) - 1)
    aux = bicchieri[el1]
    bicchieri[el1] = bicchieri[el2]
    bicchieri[el2] = aux
    print(el1,el2)

def scambia_shuffle(oggetti):
    random.sample(oggetti, k=len(oggetti))

my_bicchieri = [True,False,False]
'''
volte = random.randint(0, 10)
for _ in range(0,volte):
    scambia_due_elementi(my_bicchieri)
'''
scambia_shuffle(my_bicchieri)
print(my_bicchieri)
