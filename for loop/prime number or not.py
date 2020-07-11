""" Write a program Prime number or not """

n = int(input("Enter n = "))

flag = "not a prime number "

for i in range(2,n//2+1) :


    if n % i == 0 :
        print(flag)
        break
    else :
        print("Is the prime number")
