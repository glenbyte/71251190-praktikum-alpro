import random
import string

def generate_password(panjang=8):
    karakter = string.ascii_letters + string.digits
    return "".join(random.choices(karakter, k=panjang))

def is_email(kata):
    if kata.count("@") != 1:
        return False
    username, domain = kata.split("@")
    return bool(username) and "." in domain and not domain.startswith(".")

teks = input("Masukkan teks: ")
kata_list = teks.split()

email_list = [k.strip("(),.;") for k in kata_list if is_email(k.strip("(),.;"))]

if not email_list:
    print("Tidak ada email ditemukan.")
else:
    for email in email_list:
        username = email.split("@")[0]
        password = generate_password()
        print(f"{email} username: {username} , password: {password}")