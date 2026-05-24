def muliq():
    c_list = ["bentilap", "nekoq", "witiq ", "rerak", "tongau", "kokoq"]
    c_set = {"telakai", "puhaq", "urank", "nahat"}
    c_tuple = ("pelokaq", "marau", "engkohop", "ngkoongk")

    konversi = {
        "List → Set": (c_list, set, "list", "set"),
        "Set → List": (c_set, list, "set", "list"),
        "Tuple → Set": (c_tuple, set, "tuple", "set"),
        "Set → Tuple": (c_set, tuple, "set", "tuple")
    }

    for nama, (data, fungsi, tipe_awal, tipe_akhir) in konversi.items():
        print(f"{nama}")
        print(f"Sebelum ({tipe_awal:5}) : {data}")
        hasil = fungsi(data)
        print(f"Sesudah ({tipe_akhir:5}) : {hasil}")
        
        if tipe_awal in ["list", "tuple"] and tipe_akhir == "set":
            if len(data) != len(hasil):
                print(f"{len(data)-len(hasil)} duplikat terhapus")

if __name__ == "__main__":
    muliq()