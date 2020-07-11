""" Write a program factorial of given numbers """


n = int(input("Enter number = "))

factorial = 1

for i in range(n,1,-1) :

    factorial = factorial * i
    
print ("factorial value is = ",factorial)
    
    
