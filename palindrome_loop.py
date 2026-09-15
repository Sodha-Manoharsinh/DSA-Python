st = input().lower()
left, right = 0, len(st)-1

is_palindrome = True

while left<right:
    if st[left] != st[right]:
        is_palindrome = False
        break
    left += 1
    right -=1

print("Is palindrome: ",is_palindrome)