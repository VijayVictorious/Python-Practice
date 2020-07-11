""" Write a program count even number or between a and b

            note. a and b are user input for start and end value """

a = int(input("Enter a value = "))
b = int(input("Enter b value = "))

count = 0

for i in range(a,b+1) :

    if i % 2 == 0:

        count = count+1

print("Count even number = ",count)


