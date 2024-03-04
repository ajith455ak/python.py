a, b = 0, 1
for i in range(100):
    print(a, end=' ')
    a, b = b, a + b
