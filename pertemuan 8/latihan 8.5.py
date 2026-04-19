import re
from datetime import datetime, date

teks = input("Masukkan teks: ")
pola = r'\b(\d{4}-\d{2}-\d{2})\b'
tanggal_list = re.findall(pola, teks)

if not tanggal_list:
    print("Tidak ada tanggal ditemukan.")
else:
    hari_ini = date.today()
    
    for tgl_str in tanggal_list:
        try:
            tgl = datetime.strptime(tgl_str, "%Y-%m-%d").date()
            selisih = (hari_ini - tgl).days
            print(f"{tgl_str} 00:00:00 selisih {selisih} hari")
        except ValueError:
            print(f"{tgl_str} 00:00:00 Format tanggal tidak valid!")