n=eval(input("enter a number"))
rn=0
while(n>0):
    ones=n%10
    rn=rn*10+ones
    n=n//10
print(rn)
