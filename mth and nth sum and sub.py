numbers = list(map(int, input("Enter numbers separated by space: ").split()))
m = eval(input("Enter the value of m: "))
n = eval(input("Enter the value of n: "))
if m > len(numbers) or n > len(numbers):
    print("Error: m and n should be less than or equal to the list length.")
else:
    mth_max = sorted(numbers)[-m]
    nth_min = sorted(numbers)[n-1]
    total_sum = mth_max +  nth_min
    difference = abs(mth_max - nth_min)
    print(f"{m}th Max: {mth_max}")
    print(f"{n}th Min: {nth_min}")
    print(f"Sum of all : {total_sum}")
    print(f"Difference between {m}th Max and {n}th Min: {difference}")
