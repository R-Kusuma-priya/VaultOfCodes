def Palindrome(s):
    return s == s[::-1]
s = input()
ans = Palindrome(s)
if ans:
    print("Yes")
else:
    print("No")