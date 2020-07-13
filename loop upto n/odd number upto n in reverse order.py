""" Write a program odd number upto n in reverse order """

n = int(input("Enter n = "))

for i in range(n,0,-1) :

        for j in range(i,0,-1) :

            if j % 2!=0 :
                print("odd number upto n in reverse order = ",j)
