b= [[2, 2,2],[3, 3,3]]
a = [[3,3,3],[2,2,2]]
c= [[0, 0,0],[0, 0,0]]
for i in range(len(b)):
    for j in range(len(a[0])):
        for k in range(len(a)):
            c[i][j] += b[i][k] * a[k][j]
for i in c:
    print(i)



    
    
