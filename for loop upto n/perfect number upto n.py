""" Perfact number or not / perfect number upto n numbers """


n = int(input("Enter n = "))

sum = 0

for i in range(1,n) :

    if n % i == 0 :
        sum = 0

        for j in range(1,i) :

            if i % j == 0 :
                sum = sum + j

        if sum == i :
            print(i, "is the perfect number")

        else :
            print(i, "is not a perfect number ")
    
        
    
