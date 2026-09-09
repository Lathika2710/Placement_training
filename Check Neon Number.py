n = int(input())
square = n * n
s = 0

while square > 0:
    s += square % 10
    square //= 10

if s == n:
    print("Neon")
else:
    print("Not Neon")