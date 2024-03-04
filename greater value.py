n=eval(input("enter a number"))
m=eval(input("enter a number"))
y=eval(input("enter a number"))
if (n<m and n<y ):
    greatest=m
elif(m<n and m<y):
    greatest=m
else:
    greatest=y
print("the greater number is ",greatest)
