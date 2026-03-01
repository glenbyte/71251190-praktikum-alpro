bil1 = bil2 = bil3 = 0
try:
    bil1 = float(input("Bilangan 1: ").replace(',', '.'))
    if bil1.is_integer():
        bil1 = int(bil1)
except:
    print("Input tidak valid!")
    exit()
try:
    bil2 = float(input("Bilangan 2: ").replace(',', '.'))
    if bil2.is_integer():
        bil2 = int(bil2)
except:
    print("Input tidak valid!")
    exit()
try:
    bil3 = float(input("Bilangan 3: ").replace(',', '.'))
    if bil3.is_integer():
        bil3 = int(bil3)
except:
    print("Input tidak valid!")
    exit()
if bil1 >= bil2 and bil1 >= bil3:
    terbesar = bil1
    if bil1 == bil2 == bil3:
        print("Semua bilangan sama")
    elif bil1 == bil2:
        print(f"Bilangan 1 dan 2 terbesar: {bil1}")
    elif bil1 == bil3:
        print(f"Bilangan 1 dan 3 terbesar: {bil1}")
    else:
        print(f"Bilangan terbesar: {bil1} (bilangan 1)")
elif bil2 >= bil1 and bil2 >= bil3:
    terbesar = bil2
    if bil2 == bil3:
        print(f"Bilangan 2 dan 3 terbesar: {bil2}")
    else:
        print(f"Bilangan terbesar: {bil2} (bilangan 2)")
else:
    terbesar = bil3
    print(f"Bilangan terbesar: {bil3} (bilangan 3)")
