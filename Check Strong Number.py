n = int(input())
temp = n
s = 0

while temp > 0:
    digit = temp % 10
    fact = 1

    for i in range(1, digit + 1):
        fact *= i

    s += fact
    temp //= 10

if s == n:
    print("Strong")
else:
    print("Not Strong")