""" write a program to find wheather a number is divisible by 3 and 5 or not """

num=int(input("Enter num : "))

if(num % 3==0 and num % 5==0):
    print("value is = ",num, "is divided by 3 and 5")

else:
    print("value is = ", num ,  "is not divided by 3 and 5")
