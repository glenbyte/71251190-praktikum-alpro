# memo untuk menyimpan hasil perhitungan fungsi agar tidak dihitung ulang berkali-kali.
def combine_memo_dict(n, k, memo=None):
    if memo is None:
        memo = {}
    # biar bisa pakai tuple atau f-string
    key = (n, k)
    
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    
    if key in memo:
        return memo[key]
    
    memo[key] = combine_memo_dict(n-1, k-1, memo) + combine_memo_dict(n-1, k, memo)
    return memo[key]

print(f"C(30,15) = {combine_memo_dict(30, 15)}")
print(f"C(67,51) = {combine_memo_dict(67, 51)}")