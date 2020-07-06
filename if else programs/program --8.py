""" Greatest of four numbers using logical operator """



a=int(input("Enter a : "))
b=int(input("Enter b : "))
c=int(input("Enter c : "))
d=int(input("Enter d : "))

if a > b and a > c and a > d :
    print(a, "is the greatest value")

elif b > c and b > d :
    print(b, "is the greatest value")

elif c > d :
    print(c, "is the greatest value")

else :
    print(d, "is the greatest value")

