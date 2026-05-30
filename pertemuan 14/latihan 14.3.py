# bingung maksud soal jadi buat dua fungsi ajalah 
# v1 Deret bilangan ganjil biasa
def jumlah_ganjil_biasa(n):
    """n = jumlah suku. Contoh: n=4 → 1+3+5+7 = 16"""
    if n == 1:
        return 1
    return (2*n - 1) + jumlah_ganjil_biasa(n-1)

# v2 Deret 1, 3, 7, 15, ... (2ⁿ - 1) 
# 1 + 3 + 7 + ... + (2^n - 1) mungkin ini ya maksudnya
def jumlah_deret_2n_minus_1(n):
    """n = jumlah suku. Contoh: n=3 → 1+3+7 = 11"""
    if n == 1:
        return 1  # 2^1 - 1 = 1
    return (2**n - 1) + jumlah_deret_2n_minus_1(n-1)

for i in range(1, 6):
    print(f"{i} suku pertama: {jumlah_ganjil_biasa(i)}")
print("↑ v1" * 1)
print("=" * 40)
print("↓ v2" * 1)
for i in range(1, 6):
    print(f"{i} suku pertama: {jumlah_deret_2n_minus_1(i)}")