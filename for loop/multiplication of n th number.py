""" Write a program print Multiplication table for n th number

            eg. n=4
            output = 4 * 1 = 4
                     4 * 2 = 8
                         ...
                         ...
                         ....
                     4 * 10 = 40      """


start = int(input("Enter start number = "))
end = int(input("Enter end number = "))
n = int(input("Enter n = "))

for i in range(start,end+1) :
    print(i,"x",n,"=",i*n)


    
     



