#😴
import os
import re
def read_file(name):
    if not os.path.exists(name):
        print(f"Error: File '{name}' not found!")
        return None
    try:
        with open(name, 'r', encoding='utf-8') as f:
            return set(re.findall(r"\b[a-z]+(?:[ '-][a-z]+)*\b", f.read().lower()))
    except Exception as e:
        print(f"Error: can't read '{name}' - {e}")
        return None
def ngagau():
    print("find common words between two files")
    name1 = input("File one: ").strip()
    name2 = input("File two  : ").strip()
    word1 = read_file(name1)
    word2 = read_file(name2)
    if word1 is None or word2 is None:
        print("Program stop.")
        return  
    same_word = word1 & word2 
    print(f"{name1}: {len(word1)} unique word")
    print(f"{name2}: {len(word2)} unique word")
    print(f"same word: {len(same_word)} word")  
    if same_word:
        print(" same word:")
        for word in sorted(same_word):
            print(f"   - {word}")
    else:
        print("no two words are same")
    # Opsi simpan file 😎
    if input("Simpan ke file? (y/n): ").lower() == 'y':
        kereheng = input("Name file [hasil.txt]: ").strip() or "hasil.txt"
        try:
            with open(kereheng, 'w', encoding='utf-8') as f:
                f.write(f"same word between{name1} and {name2}:\n")
                f.write("\n".join(f"  {k}" for k in sorted(same_word)))
            print(f"save to {kereheng}")
        except Exception as e:
            print(f"save failed: {e}") 
    print("finish")
if __name__ == "__main__":
    ngagau()