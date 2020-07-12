""" Write a program print prime numbers upto n """


n = int(input("Enter n = "))

for i in range(2,n+1) :

    flag = "not a prime number"

    for j in range(2,i+1) :

        if i % j == 0 :
            print(flag)
            break
        else :
            print("Is the prime number")
