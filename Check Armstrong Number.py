n = int(input())
temp = n
digits = len(str(n))
s = 0

while temp > 0:
    digit = temp % 10
    s += digit ** digits
    temp //= 10

if s == n:
    print("Armstrong")
else:
    print("Not Armstrong")