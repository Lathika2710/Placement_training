n = int(input())
temp = n
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

if rev == n:
    print("Palindrome")
else:
    print("Not Palindrome")