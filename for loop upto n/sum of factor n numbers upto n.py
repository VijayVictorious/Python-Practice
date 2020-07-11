""" Write a program sum of factor n numbers upto n """


n = int(input("Enter n = "))

for i in range(1,n+1) :
    sum = 0

    for j in range(1,i+1) :
        sum = sum + j
    print(" sum of factor upto n = ",sum)
