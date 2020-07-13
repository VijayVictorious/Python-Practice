""" Write a program sum of natural numbers upto n """


n = int(input("Enter n = "))

for i in range(1,n+1) :
    sum = 0

    for j in range(1,i+1) :
        sum = sum + j

    print("sum of natural number upto n = ",sum)
