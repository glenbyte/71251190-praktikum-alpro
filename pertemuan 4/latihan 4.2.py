def cek_bilangan(angka):
    """kembalikan 'Positif', 'Negatif', atau 'Nol' tergantung angka yang dimasukkan"""
    return "Positif" if angka > 0 else ("Negatif" if angka < 0 else "Nol")

data_uji = [40, -20, 0]
hasil_yang_diharapkan = ["Positif", "Negatif", "Nol"]
print("\n| Input | Output Program | Output Diharapkan | Status |")

for i in range(len(data_uji)):
    bilangan = data_uji[i]
    hasil_program = cek_bilangan(bilangan)
    hasil_harapan = hasil_yang_diharapkan[i]
    status = "✓" if hasil_program == hasil_harapan else "✗"
    
    print(f"| {bilangan:5} | {hasil_program:13} | {hasil_harapan:17} |   {status}   |")