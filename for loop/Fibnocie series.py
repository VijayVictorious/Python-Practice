""" Write a program Fibnocie series 0 1 1 2 3 5 8 13 .... n """



n = int(input("Enter n = "))
first = 1
for i in range(0,n+1) :
    first = first + i
    print("Fibnocie series = ",first)
   


