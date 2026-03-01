
try:
    print("S1: ", end="")
    s1_str = input().strip()
    if s1_str == "":
        print("S1 tidak boleh kosong")
    else:
        s1 = float(s1_str)
        if s1 <= 0:
            print("S1 harus besar dari 0")
        else:
            print("S2: ", end="")
            s2_str = input().strip()
            if s2_str == "":
                print("S2 tidak boleh kosong")
            else:
                s2 = float(s2_str)
                if s2 <= 0: 
                    print("S2 harus besar dari 0")
                else:
                    print("S3: ", end="")
                    s3_str = input().strip()
                    if s3_str == "":  
                        print("S3 tidak boleh kosong")
                    else:
                        s3 = float(s3_str)
                        if s3 <= 0:  
                            print("S3 harus besar dari 0")
                        else:                         
                            print("Data sisi yang dimasukkan:")
                            print("S1: " + str(s1))
                            print("S2: " + str(s2))
                            print("S3: " + str(s3))                                                
                            print("JENIS BERDASARKAN SISI:")
                            if s1 == s2 == s3:
                                print("3 sisi sama (Segitiga Sama Sisi)")
                            elif s1 == s2 or s1 == s3 or s2 == s3:
                                print("2 sisi sama (Segitiga Sama Kaki)")
                            else:
                                print("Tidak ada yang sama (Segitiga Sembarang)")                        
except ValueError:
       print("Harus masukkan angka")
       