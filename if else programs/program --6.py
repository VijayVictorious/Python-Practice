""" write a program greatest of three numbers """

a=int(input("Enter a : "))
b=int(input("Enter b : "))
c=int(input("Enter c : "))

if a > b :
    if a > c :
        print(a, "is the greatest value")

    else:
        print(c, "is the greatest value")

elif b > c :
    print(b, "is the greatest value")

else:
    print(c, "is the greatest value")
