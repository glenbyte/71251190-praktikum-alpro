kata1 = input("Masukkan kata pertama: ").lower().replace(" ", "")
kata2 = input("Masukkan kata kedua: ").lower().replace(" ", "")

if len(kata1) != len(kata2):
    print(f"BUKAN anagram (panjang berbeda)")
else:
    list_kata2 = list(kata2)
    anagram = True
    idx = 0
    
    while idx < len(kata1) and anagram:
        huruf = kata1[idx]
        if huruf in list_kata2:
            list_kata2.remove(huruf)
        else:
            anagram = False
        idx += 1
    
    print(f"ANAGRAM" if anagram else "BUKAN ANAGRAM")
    #replace() digunakan untuk mengganti suatu substring (bagian dari string) dengan substring lain.