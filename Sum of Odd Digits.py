n = int(input())
s = 0

while n > 0:
    digit = n % 10

    if digit % 2 != 0:
        s += digit

    n //= 10

print(s)