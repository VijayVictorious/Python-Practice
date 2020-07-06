""" Greatest of three numbers using logical operator """


a=int(input("Enter a : "))
b=int(input("Enter b : "))
c=int(input("Enter c : "))

if a > b  and  a > c :
    print(a, " is the greatest value")

elif b > c :
    print(b, " is the greatest value")

else :
    print(c, " is the greatest value")
