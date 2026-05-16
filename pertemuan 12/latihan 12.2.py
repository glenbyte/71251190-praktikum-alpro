def proses_data(data):
    nama, nim, alamat = data
    print(f"Data: {data}")
    print(f"NIM : {nim} ")
    print(f"NAMA : {nama}")
    print(f"ALAMAT : {alamat}")
    print(f"NIM : {tuple(nim)}")
    
    depan = nama.split()[0]
    print(f"NAMA DEPAN: {tuple(depan)}")
    
    terbalik = tuple(nama.split()[::-1])
    print(f"NAMA TERBALIK: {terbalik}")

dasiswa = ('Matahari Bhakti Nendya', '22064091', 'Bantul, DI Yogyakarta')
proses_data(dasiswa)