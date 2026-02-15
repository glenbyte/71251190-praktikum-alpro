gaji_perjam = int(input("Masukkan Gajinya Budi: "))
jam_kerja = float(input("Masukkan jam kerja perminggu Budi: "))
minggu = 5
pendapatan_sebelum_pajak = gaji_perjam * jam_kerja * minggu
pendapatan_sesudah_pajak = pendapatan_sebelum_pajak - ((pendapatan_sebelum_pajak * 14) / 100)
uang_pakaian_dan_aksesoris = 0.10 * pendapatan_sesudah_pajak
uang_alat_tulis = 0.01 * pendapatan_sesudah_pajak
total_pengeluaran = pendapatan_sesudah_pajak - uang_pakaian_dan_aksesoris - uang_alat_tulis
uang_sedekah = 0.25 * total_pengeluaran
uang_anak_yatim = 0.30 * uang_sedekah
uang_kaum_dhuafa = uang_sedekah - uang_anak_yatim
print("Pendapatan Budi selama libur musim panas sebelum melakukan pembayaran pajak:", pendapatan_sebelum_pajak)
print("Pendapatan Budi selama libur musim panas setelah melakukan pembayaran pajak:", pendapatan_sesudah_pajak)
print("Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris: ", uang_pakaian_dan_aksesoris)
print("Jumlah uang yang akan Budi habiskan untuk membeli alat tulis: ", uang_alat_tulis)
print("Jumlah uang yang akan Budi sedekahkan:", uang_sedekah)
print("Jumlah uang yang akan diterima anak yatim: ", uang_anak_yatim)
print("Jumlah uang yang akan diterima kaum dhuafa", uang_kaum_dhuafa)