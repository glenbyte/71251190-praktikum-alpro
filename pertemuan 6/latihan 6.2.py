def ganjil(bawah, atas):
    if bawah < atas:
        print(f"bawah = {bawah}, atas = {atas}. Karena bawah < atas, berarti dari kecil ke besar, maka hasilnya adalah: ", end="")
        i = bawah
        while i <= atas:
            if i % 2 != 0:
                print(i, end=" ")
            i += 1
        print()  
    else:
        print(f"bawah = {bawah}, atas = {atas}. Karena bawah > atas, berarti dari besar ke kecil, maka hasilnya adalah: ", end="")
        i = bawah
        while i >= atas:
            if i % 2 != 0:
                print(i, end=" ")
            i -= 1
        print()  

bawah = int(input("Masukkan batas bawah: "))
atas = int(input("Masukkan batas atas: "))
ganjil(bawah, atas)