parole = ["All", "work", "and", "no", "play", "makes", "Folcarelli", "a", "dull", "boy"]

## trova parola più lunga
max_len = 0
for parola in parole:
    if len(parola) > max_len:
        max_len = len(parola)
        
        
array = [5,3,-1,4,0]
min_value = array[0] # salvo in min value il primo elemento dell'array

for numero in array:
    if numero < min_value: ## se numero è minore del minore fino ad ora raggiunto
        min_value = numero 
        
print(min_value)


print("max: ", min(array))
print("max: ", min(1,20,9,3,8)) # sono due concetti molto diversi