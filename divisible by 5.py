n=int(input("enter a number :"))
numbers=range(1,n+1,1)
for num in numbers:
      if (num%5==0):
          print(num,"  is divisible by 5 ")
      else:
          print(num," is not divisible by 5")
