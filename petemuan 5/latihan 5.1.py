def cek_angka(a, b, c):
    return (a != b and a != c and b != c) and (a + b == c or a + c == b or b + c == a)

print(cek_angka(4, 6, 10)) 
print(cek_angka(2, 2, 4))  
print(cek_angka(15, 8, 7))
print(cek_angka(20, 10, 10))