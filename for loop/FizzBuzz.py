""" Write a for loop program FizzBuzz """


n = int(input("Enter number = "))

for i in range(1,n+1) :

    if i % 3 == 0 and i % 5 == 0 :
        print("Fizz Buzz")

    elif i % 3 == 0 and i % 5!=0 :
        print("Fizz")

    elif i % 3!=0 and i % 5 == 0 :
        print("Buzz")

    else :
        print(i)


