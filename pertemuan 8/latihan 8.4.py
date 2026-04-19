kalimat = input("Masukkan kalimat: ")
kata_list = kalimat.split()

if not kata_list:
    print("Kalimat kosong!")
else:
    terpendek = kata_list[0]
    terpanjang = kata_list[0]
    
    for i in range(len(kata_list)):
        if len(kata_list[i]) < len(terpendek):
            terpendek = kata_list[i]
        if len(kata_list[i]) > len(terpanjang):
            terpanjang = kata_list[i]
    
    print(f"terpendek: {terpendek}")
    print(f"terpanjang: {terpanjang}")