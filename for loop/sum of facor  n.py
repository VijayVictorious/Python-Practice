""" Write a program sum of factor "n"

            eg. n=6
            output = (because factor of 6 is 1,2,3,6,then sum of these factor is 1+2+3+6 = 12)

            eg 2. n=8
            output = 15(1+2+4+8 = 15) """


start = int(input("Enter start value = "))
end = int(input("Enter end value = "))
n = int(input("Enter n = "))
sum = 0

for i in range(start,end+1) :
    sum = sum + i


    if n % i == 0 :
        print(sum)







