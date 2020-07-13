""" Write a program factor of n numbers upto n """


n = int(input("Enter n = "))

for i in range(1,n+1) :

        for j in range(1,i+1) :

            if i % j == 0 :
                print("factor of n numbers upto n = ",j)
