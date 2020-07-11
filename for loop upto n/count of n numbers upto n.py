""" Write a program count of n numbers upto n """

n = int(input("Enter count number = "))

count = 0

for i in range(1,n+1) :
    count = 0

    for j in range(1,i+1) :
        print(j)
        count = count + 1
        
    print("Count value is = ",count)
