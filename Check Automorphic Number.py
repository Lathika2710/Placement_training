n = int(input())

square = n * n

if square % (10 ** len(str(n))) == n:
    print("Automorphic")
else:
    print("Not Automorphic")