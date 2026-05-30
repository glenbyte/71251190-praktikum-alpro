def palindrome_recursive(kalimat, left, right):
    if left >= right:
        return True
    if kalimat[left] != kalimat[right]:
        return False
    return palindrome_recursive(kalimat, left + 1, right - 1)

def cek_palindrome(kalimat):
    return palindrome_recursive(kalimat, 0, len(kalimat) - 1)
# Contoh
print(cek_palindrome("kodok"))  
print(cek_palindrome("hello"))  
print(cek_palindrome("level")) 
print(cek_palindrome("aku gue"))