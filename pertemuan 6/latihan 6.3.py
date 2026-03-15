jumlah_mk = int(input("Jumlah mata kuliah: "))

total_bobot = 0
total_sks = 0
sks_per_mk = 3  
for i in range(1, jumlah_mk + 1):
    print(f"Mata Kuliah ke-{i}")
    nilai = input(f"Nilai MK {i} (A/B/C/D): ")
    
    if nilai == 'A':
        bobot = 4
    elif nilai == 'B':
        bobot = 3
    elif nilai == 'C':
        bobot = 2
    elif nilai == 'D':
        bobot = 1
    else:
        print("Nilai Salah Masukkan A, B, C, atau D.")
        bobot = 0
        continue
    total_bobot += bobot * sks_per_mk
    total_sks += sks_per_mk
if total_sks > 0:
    ips = total_bobot / total_sks
    print(f"Total Bobot      : {total_bobot}")
    print(f"Total SKS        : {total_sks}")
    print(f"Indeks Prestasi Semester (IPS) : {ips:.2f}")
else:
    print("Tidak ada data mata kuliah yang valid")