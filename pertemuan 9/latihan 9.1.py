#ambatunat 🗿
import os

file1 = "ple1.txt"
file2 = "ple2.txt"

print("PROGRAM PEMBANDING FILE TEKS")
print(f"File pertama : {file1}")
print(f"File kedua   : {file2}")

file1_ada = os.path.exists(file1)
file2_ada = os.path.exists(file2)

print("\nSTATUS FILE:")
print(f"File 1 '{file1}': {'✓ DITEMUKAN' if file1_ada else '✗ TIDAK DITEMUKAN'}")
print(f"File 2 '{file2}': {'✓ DITEMUKAN' if file2_ada else '✗ TIDAK DITEMUKAN'}")

if file1_ada and file2_ada:
    try:
        with open(file1, "r", encoding="utf-8") as f1:
            baris_file1 = f1.readlines()
        
        with open(file2, "r", encoding="utf-8") as f2:
            baris_file2 = f2.readlines()
        
        print("\nHASIL PERBANDINGAN:")
        max_baris = max(len(baris_file1), len(baris_file2))
        
        ada_perbedaan = False
        jumlah_perbedaan = 0     
        for i in range(max_baris):
            if i < len(baris_file1):
                baris1 = baris_file1[i].rstrip('\n')
            else:
                baris1 = "(FILE 1 TIDAK ADA BARIS)"      
            if i < len(baris_file2):
                baris2 = baris_file2[i].rstrip('\n')
            else:
                baris2 = "(FILE 2 TIDAK ADA BARIS)"
            if baris1 != baris2:
                ada_perbedaan = True
                jumlah_perbedaan += 1
                print(f"\nBaris ke-{i+1}:")
                print(f"  File 1: {baris1}")
                print(f"  File 2: {baris2}")
                print(f"  Status: BERBEDA")

        if not ada_perbedaan:
            print("KESIMPULAN: Kedua file SAMA PERSIS! Tidak ada perbedaan.")
        else:
            print(f"KESIMPULAN: Ditemukan {jumlah_perbedaan} baris yang berbeda.")   

    except Exception as e:
        print(f"\nERROR SAAT MEMBACA FILE: {e}")

else:
    print("\nERROR: FILE TIDAK DITEMUKAN!")

    if not file1_ada:
        print(f"✗ File '{file1}' tidak ditemukan.")
        print(f"   Pastikan file ada di folder: {os.getcwd()}")
    
    if not file2_ada:
        print(f"✗ File '{file2}' tidak ditemukan.")
        print(f"   Pastikan file ada di folder: {os.getcwd()}")
    
    print("\nSOLUSI:")
    print("1. Buat file 'ple1.txt' dan 'ple2.txt' di folder ini")
    print("2. Pastikan nama file tepat (huruf kecil semua)")
    print("3. Letakkan file di folder yang sama dengan program ini")
    print(f"4. Folder saat ini: {os.getcwd()}")
    print("\nFILE .txt YANG ADA DI FOLDER INI:")
    file_txt = [f for f in os.listdir('.') if f.endswith('.txt')]
    if file_txt:
        for f in file_txt:
            print(f"  - {f}")
    else:
        print("  (Tidak ada file .txt)")
    buat_file = input("Apakah Anda ingin membuat file?(ple1.txt dan ple2.txt)? (y/n): ").lower()
    if buat_file == 'y':
        with open("ple1.txt", "w", encoding="utf-8") as f:
            f.write("Baris 1: kepai bi ewah muliq\n")
            f.write("Baris 2: kuman nincak boleq\n")
            f.write("Baris 3: nau tih petak\n")
            f.write("Baris 4: buday\n")
            f.write("Baris 5: rungan")

        with open("ple2.txt", "w", encoding="utf-8") as f:
            f.write("Baris 1: lelai akuq ewah muliq\n")
            f.write("Baris 2: muruq anum siq\n")
            f.write("Baris 3: nau tih kedup\n")
            f.write("Baris 4: buoq \n")
            f.write("Baris 5: rengan\n")
        
        print("\n✓ File ple1.txt dan ple2.txt telah dibuat!")
        print("  Silakan jalankan program kembali.")