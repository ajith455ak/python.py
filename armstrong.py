for n in range(1, 1001):
    x = len(str(n))
    sum = 0
    a = n
    while (a > 0):
        y = (a % 10)
        sum += y ** x
        a //= 10
    if n == sum:
        print(n)
