def is_prima_limit(n, pembagi=2):
    # hanya cek sampai akar n
    import math
    limit = int(math.sqrt(n)) + 1
    
    if n < 2:
        return False
    if pembagi >= limit:
        return True
    if n % pembagi == 0:
        return False
    return is_prima_limit(n, pembagi + 1)

print(is_prima_limit(67))  
print(is_prima_limit(20))  