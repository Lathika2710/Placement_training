a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a <= b and a <= c:
    print("smallest:",a)
elif b <=a and b <= c:
    print("smallest:",b)
else:
    print("smallest:",c)