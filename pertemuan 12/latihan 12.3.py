nama_file = input("Enter a file name: ")
jam_counts = {}
try:
    with open(nama_file, 'r') as file:
        for baris in file:
            if baris.startswith('From '):
                kata = baris.split()
                if len(kata) > 5: 
                    waktu = kata[5]
                    jam = waktu[:2]
                    jam_counts[jam] = jam_counts.get(jam, 0) + 1
    for jam in sorted(jam_counts.keys()):
        print(jam, jam_counts[jam])
except FileNotFoundError:
    print(f"File '{nama_file}' tidak ditemukan.")
#fungsi get pada dictionary Python untuk mengambil nilai berdasarkan key, dengan aman