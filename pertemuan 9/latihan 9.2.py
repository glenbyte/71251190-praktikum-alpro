# Auto create file jika belum ada
import os
#digunakan untuk mengakses fungsi-fungsi sistem operasi, seperti mengelola file, folder, path, dan lingkungan sistem.
nama_file = "soal.txt"
# Buat file jika belum ada
#os.path.exists() adalah fungsi dari os digunakan untuk mengecek sebuah file atau direktori ada di komputer.
if not os.path.exists(nama_file):
    print(f"File {nama_file} tidak ditemukan. Membuat file baru...")
    with open(nama_file, "w", encoding="utf-8") as f:
        f.write("1+1 = || 2\n")
        f.write("Bendera Indonesia? || Merah Putih\n")
        f.write("Kota gudeg adalah: || Yogyakarta\n")
        f.write("Komponen PC untuk penyimpanan file adalah... || harddisk\n")
        f.write("50 * 20 = || 1000\n")
    print(f"File {nama_file} berhasil dibuat!\n")
print(f"nama file1: {nama_file}")
# Baca dan proses file
with open(nama_file, "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        if baris == "" or "||" not in baris:
            continue
        pertanyaan, jawaban_benar = baris.split("||", 1)
        pertanyaan = pertanyaan.strip()
        jawaban_benar = jawaban_benar.strip()
        print(pertanyaan)
        jawaban_user = input("Jawab: ").strip()
        
        if jawaban_user.lower() == jawaban_benar.lower():
            print("Jawaban benar!\n")
        else:
            print(f"Jawaban salah! (Jawaban benar: {jawaban_benar})\n")
#encoding adalah parameter yang menentukan format karakter yang digunakan saat membaca atau menulis file
