def jumlah_digit(angka_str):
    if len(angka_str) == 1:
        return int(angka_str)
    return int(angka_str[0]) + jumlah_digit(angka_str[1:])

# Contoh soal
print(jumlah_digit("234"))   