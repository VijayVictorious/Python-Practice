""" Write a program print the odd number up to n in reverse order 

            eg. n=10
            ouuput = 9,7,5,3,1 """


n = int(input("Enter number = "))

for i in range(10,0,-1) :

    if i % 2!=0 :
        print(i)
    


