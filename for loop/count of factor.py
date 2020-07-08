""" Write a program Count of factor

            eg. n=6
            output = 4(because 6 has four factor like 1,2,3,6 ) """


n = int(input("Enter factor value = "))

count = 0

for i in range(1,n+1) :

    if n % i == 0 :
        count = count +1
print("Count of factor = ",count)
    
