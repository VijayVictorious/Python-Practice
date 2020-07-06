"""
input--> p,r,n,ci

p--> principle
r--> rate of intrest
n--> no. of years
ci--> compound intrest

process

ci=p*pow(1+r/100,n)-p

"""

p=int(input("Enter P: "))
r=int(input("Enter r: "))
n=int(input("Enter n: "))
ci=p*pow(1+r/100,n)-p
print("compound intrest = ",ci)
print(type(p,n,r))
