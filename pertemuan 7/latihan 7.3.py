def tampilkan_deret(tinggi, lebar):
    for i in range(tinggi):
        for j in range(lebar):
            print(i * lebar + j + 1, end=" " if j < lebar - 1 else "")
        print()
try:
    tinggi = int(input("Masukkan tinggi: "))
    lebar = int(input("Masukkan lebar: "))
    
    if tinggi > 0 and lebar > 0:
        tampilkan_deret(tinggi, lebar)
    else:
        print("Tinggi dan lebar harus lebih dari 0!")
except ValueError:
    print("Input harus angka!")