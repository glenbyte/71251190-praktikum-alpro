print("JUMLAH HARI - TAHUN 2020")
print("-" * 30)

try:
    bulan = int(input("Masukkan bulan (1-12): "))
    
    if 1 <= bulan <= 12:
        if bulan == 2:
            hari = 29
        elif bulan in [4, 6, 9, 11]:
            hari = 30
        else:
            hari = 31
        
        print("Jumlah hari: " + str(hari))
    else:
        print("hanya Bulan 1-12")
        
except ValueError:
    print("harus masukkan angka")
