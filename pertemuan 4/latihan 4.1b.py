def cek_bilangan(angka):
    """bilangan positif, negatif, atau nol"""
    if angka > 0:
        return "Positif"
    elif angka < 0:
        return "Negatif"
    else:
        return "Nol"
def main():
    try:       
            user_input = input("Masukkan bilangan: ")          
            user_input = user_input.strip()       
            try:   
                if ',' in user_input:
                    user_input = user_input.replace(',', '.')
                    print("(Mengganti koma menjadi titik untuk desimal)")   
                bilangan = float(user_input)   
                if bilangan.is_integer():
                    bilangan = int(bilangan)        
            except ValueError:
                raise ValueError(f"'{user_input}' bukan bilangan yang valid") 
            hasil = cek_bilangan(bilangan)
            print(f"\n✓ Hasil: Bilangan {bilangan} adalah {hasil.upper()}")  
            if hasil == "Positif":
                print("   (Bilangan besar dari 0)")
            elif hasil == "Negatif":
                print("   (Bilangan kecil dari 0)")
            else:
                print("   (Bilangan sama dengan 0)")      
    except ValueError as ve:         
            print("  Masukkan bilangan yang valid ")
if __name__ == "__main__":
    main()