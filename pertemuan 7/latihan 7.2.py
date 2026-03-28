import math

n = int(input("Masukkan n: "))

i = n
while i >= 1:
    print(math.factorial(i), end=" ")
    
    j = i
    while j >= 1:
        print(j, end=" " if j > 1 else "")
        j -= 1
    
    print()
    i -= 1