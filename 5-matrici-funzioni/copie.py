var1 = 20
var2 = var1

print(var1, var2)

var1 = 10

print(var1, var2)

## con array così non creo una copia

var1 = [0,0,0]
var2 = var1
var3 = var1[:]

print(var1, var2, var3)

var1[0] = 1

print(var1, var2, var3)

# var1[:] shallow copy
array = [1,2,3]
shallow_copy = []

for i in array:
    shallow_copy.append(i)
    
print(array, shallow_copy)