def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True
def find_nearest_prime_below(n):
    if n <= 2:
        return None 
    for num in range(n - 1, 1, -1):
        if is_prime(num):
            return num
    return None
def main():
    try:
        n = int(input("Masukkan bilangan n: "))
        if n <= 2:
            print(f"Tidak ada bilangan prima yang kurang dari {n}")
        else:
            nearest_prime = find_nearest_prime_below(n)
            print(f"Bilangan prima terdekat yang kurang dari {n} adalah: {nearest_prime}")
    except ValueError:
        print("salah: Masukkan bilangan bulat yang benar!")

if __name__ == "__main__":
    main()