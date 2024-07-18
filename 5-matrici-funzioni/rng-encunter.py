import random
incontri = ["niente", "un tesoro", "un goblin", "un troll", "uno zombie", "un potentissimo necromante"]
#rng = random.randint(0,len(incontri) - 1)
rng_encunter = random.choice(incontri)
print("Davanti a te trovi", rng_encunter)