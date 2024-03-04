a=input("enter a string")
vowels=0
constant=0
for char in a:
    if char.lower() in "aeiou":
        vowels +=1
    elif char.isalpha():
        constant +=1
    print("no of vowels" ,vowels)
    print(" no of constant",constant)
        
