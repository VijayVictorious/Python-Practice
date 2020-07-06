""" Write a program print the number is divisible by 5 and 3, in between start value to end value

        note : you need to get input for start and end value from user """


start = int(input("Enter start value = "))
end = int(input("Enter end value = "))

for i in range(start,end+1) :

    if i % 5 == 0 and i % 3 ==0 :
        print(i)
