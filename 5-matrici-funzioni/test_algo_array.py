from algo_array import *

if max([8, 2, 3, 47, 77]) == 77:
    print("Test 1 superato!")
else:
    print("Test 1 fallito")
    
if max([8, -9, 3]) == 8:
    print("Test 2 superato!")
else:
    print("Test 2 fallito")
    
if max([]) == 0:
    print("Test 3 superato!")
else:
    print("Test 3 fallito")
    
if remove([1,2,3,4], 1) == [2,3,4]:
    print("Test 4 superato!")
else:
    print("Test 4 fallito")
    
print(min([7, 2, 3, 47, 77]))
print(avg([7, 2, 3, 47, 77]))
print(somma(2,4,5))