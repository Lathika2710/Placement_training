a = int(input("Enter the first number: "))
b = int(input("Enter the second nuber: "))
c = int(input("Enter the third number: "))

if a >= b and a >= c:
    print("Largest:",a)
elif b >= a and b >= c:
    print("Largest:",b)
else:
    print("Largest:",c)