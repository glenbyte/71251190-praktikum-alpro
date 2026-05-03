def  read_and_show_unique_word(name_file):
    try:
        with open(name_file, 'r', encoding='utf-8') as file:
            teks = file.read()

        import re
        words = re.findall(r'\b\w+\b', teks.lower())
        
        unique_word = sorted(set(words))
        
        print(f"Kata Unik dalam File '{name_file}' ")
        print(f"Total kata unik ditemukan: {len(unique_word)} kata\n")
        
        i = 1
        for word in unique_word:
            print(f"{i:3}. {word}")
            i += 1
            
    except FileNotFoundError:
        print(f"Error: File '{name_file}' tidak ditemukan!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    name_file = input("insert file teks : ")
    read_and_show_unique_word(name_file)