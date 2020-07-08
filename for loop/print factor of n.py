""" Write a program print factor of "n"

            eg. n=6
            output = 1,2,3,6
            explain : these output are divisor for that n means (6)  """

n = int(input("Enter n = "))

for i in range(1,n+1) :
 
    if n % i == 0 :
        print(i)    

        

    
