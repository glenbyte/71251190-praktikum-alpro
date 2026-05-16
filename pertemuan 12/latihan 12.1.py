def checking(t):
    if len(t) <= 1:
        return True
    i = 1
    while i < len(t):
        if t[i] != t[0]:
            return False
        i += 1
    return True
nekoq = (90, 90, 90, 90)
print(checking(nekoq))  
#!= tidak sama dengan di operator perbandingan