def hitung_email_dari_file(nama_file):
    try:
        with open(nama_file, 'r') as file:
            email_dict = {}  
            for line in file:
                if line.startswith('From '):
                    kata = line.split()
                    if len(kata) > 1:
                        email = kata[1]
                        email_dict[email] = email_dict.get(email, 0) + 1    
        return email_dict
    except FileNotFoundError:
        print(f"File {nama_file} tidak ditemukan.")
        return None
def main():
    nama_file = input("Masukkan nama file : ") 

    hasil = hitung_email_dari_file(nama_file)
    
    if hasil:
        print(hasil)
if __name__ == "__main__":
    main() 