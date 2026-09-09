n = int(input())
found = False

while n > 0:
    if n % 10 == 0:
        found = True
        break

    n //= 10

if found:
    print("Contains 0")
else:
    print("Does not contain 0")