try:             
            ukuran_suhu = input("Masukkan suhu tubuh: ")     
            suhu = int(ukuran_suhu)
            if suhu < 30 or suhu > 45:
                print("Suhu yang dimasukkan tidak normal untuk demam")
        
            if suhu >= 38:
                status = "DEMAM"
                print(f" Suhu tubuh Anda {suhu}°C")
                print("  Anda DEMAM.")
                print("  segera cek ke dokter.")
            else:
                status = "TIDAK DEMAM"
                print(f" Suhu tubuh Anda {suhu:.1f}°C")
                print(" TIDAK DEMAM")
                print("  Tetap jaga kesehatan dan istirahat yang cukup.")                   
except ValueError:          
            print(" invalid input")
            print("  masukan angka suhu")
           
       