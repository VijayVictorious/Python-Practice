""" write a program to find whether a number is divisible by 5 but not by 7 or not """

num=int(input("Enter num: "))

if num % 5==0 and num % 7!=0 :
    print("value : ", num , "is divided by 5 but not divided by 7")

else:
    print("value : ", num , "is divided by both 5 and 7")
