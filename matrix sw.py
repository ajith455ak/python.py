a=[[1,2,6],[2,3,4],[7,8,9]]
c=[[0,0,0 ],[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(a)):
        c[i][j]=a[j][i]
for i in c:
    print(i)
