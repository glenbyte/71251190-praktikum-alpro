def tiga_terbaik_manual(list_bilangan):
    if len(list_bilangan) < 3:
        return "List harus ada minimal 3 bilangan"
    
    tiga_tertinggi = []
    for i in range(3):
        maks = max(list_bilangan)
        tiga_tertinggi.append(maks)
        list_bilangan.remove(maks)
    
    return tiga_tertinggi

#Contoh 
bilangan = [54, 21, 96, 64, 27, 13, 10, 88]
hasil = tiga_terbaik_manual(bilangan)
print(f"3 bilangan terbaik: {hasil}")  # Output: [96, 88, 64]
print(f"List yang asli : {bilangan}")  # Output: [54, 21, 27, 13, 10] (berubah)