""" Write a program sum of factor "n"

            eg. n=6
            output = (because factor of 6 is 1,2,3,6,then sum of these factor is 1+2+3+6 = 12)

            eg 2. n=8
            output = 15(1+2+4+8 = 15) """

n = int(input("Enter factor value = "))
sum = 0

for i in range(1,n+1) :

    if n % i == 0 :
        sum = sum + i

print("Sum of factor value = ",sum)







