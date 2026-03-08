def cek_digit_belakang(a, b, c):
   
    return (a % 10 == b % 10) or (a % 10 == c % 10) or (b % 10 == c % 10)

print("Masukkan tiga bilangan:")
a = int(input("Bilangan 1: "))
b = int(input("Bilangan 2: "))
c = int(input("Bilangan 3: "))

print(f"Hasil: {cek_digit_belakang(a, b, c)}")