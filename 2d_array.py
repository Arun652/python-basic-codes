l=[]
l2=[]
for i in range(6):
    a = list(map(int,input().strip().split()))[:6]
    l.append(a)
for i in range(0,4):
    for j in range(0,4):
        sum=(l[i][j]+l[i][j+1]+l[i][j+2])+(l[i+1][j+1])+(l[i+2][j]+l[i+2][j+1]+l[i+2][j+2])
        l2.append(sum)
c=sorted(l2)
print(*c[-1:])
