def hitung_domain_dari_file(file_name):
    try:
        with open(file_name, 'r') as file:
            domain_dict = {}  
            for line in file:
                if line.startswith('From '):
                    kata = line.split()
                    if len(kata) > 1:
                        email = kata[1]
                        if '@' in email:
                            domain = email.split('@')[1]
                            domain_dict[domain] = domain_dict.get(domain, 0) + 1
        return domain_dict
    except FileNotFoundError:
        print(f"File {file_name} tidak ditemukan.")
        return None
def main():
    nama_file = input("Masukkan nama file: ")
    hasil = hitung_domain_dari_file(nama_file)
    if hasil:
        print(hasil)
if __name__ == "__main__":
    main()