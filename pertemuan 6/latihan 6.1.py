def perkalian(a, b):
    hasil = 0
    i = 0
    
    print(f"{a} x {b} = ", end="")
    
    while i < a:
        hasil += b
        print(b, end="")
        
        if i < a - 1:
            print(" + ", end="")
        else:
            print(" = ", end="")
        
        i += 1
    
    print(hasil)
    return hasil

#Contoh seperti disoal 
perkalian(6, 5)
perkalian(7, 10)