import re

def hitung_frekuensi_kata(kalimat, kata_cari):
    kalimat_bersih = re.sub(r'[^\w\s]', ' ', kalimat)
    kalimat_bersih = kalimat_bersih.lower()
    kata_cari = kata_cari.lower()
    
    daftar_kata = kalimat_bersih.split()
    jumlah = daftar_kata.count(kata_cari)
    
    return jumlah

# Contoh penggunaan
kalimat = "Saya mau makan. Makan itu wajib. Mau siang atau malam saya wajib makan"
kata = "makan"
print(f"{kata} ada {hitung_frekuensi_kata(kalimat, kata)} buah")