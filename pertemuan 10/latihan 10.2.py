list_num = []

while True:
    masukan = input("Bilangan: ")
    
    if masukan == 'done':
        break
    
    try:
        bilangan = float(masukan)
        list_num.append(bilangan)
    except:
        print("Masukkan bilangan yang valid!")

if len(list_num) > 0:
    total = 0
    for num in list_num:
        total = total + num
    
    rata_rata = total / len(list_num)
    print(f"\nTotal bilangan: {len(list_num)}")
    print(f"Jumlah semua bilangan: {total}")
    print(f"Rata-rata: {rata_rata}")
else:
    print("Tidak ada data untuk dihitung.")