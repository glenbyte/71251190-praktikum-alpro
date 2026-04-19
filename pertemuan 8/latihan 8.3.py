kalimat = input("Masukkan kalimat: ")

hasil = ""
sebelumnya_spasi = False

for karakter in kalimat:
    if karakter == " ":
        if not sebelumnya_spasi:
            hasil += karakter
            sebelumnya_spasi = True
    else:
        hasil += karakter
        sebelumnya_spasi = False

hasil = hasil.strip()

print(f"Hasil: {hasil}")