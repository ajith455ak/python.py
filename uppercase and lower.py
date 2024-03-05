def count_chars():
    lower_case = 0
    upper_case = 0
    numbers = 0
    while True:
        char = input("Enter any character: ")
        if char == '*':
            break
        elif char.islower():
            lower_case += 1
        elif char.isupper():
            upper_case += 1
        elif char.isdigit():
            numbers += 1
    return lower_case, upper_case, numbers
lower_case, upper_case, numbers = count_chars()
print("Total count of lower case:", lower_case)
print("Total count of upper case:", upper_case)
print("Total count of numbers:", numbers)
