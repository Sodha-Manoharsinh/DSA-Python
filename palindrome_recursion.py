def check_palindrome(s,left,right):
    print(f"check_palindrome({s},{left},{right})")
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return check_palindrome(s,left+1,right-1)

st = input().lower()
res = check_palindrome(st,0,len(st)-1)
print("Is palindrome: ",res)