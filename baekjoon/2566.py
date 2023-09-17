a = [list(map(int, input().split())) for _ in range(9)]
b =[[a[0][0]], [0,0]]

for i in range(len(a)) :
    for j in range(len(a[i])) :
        if a[i][j] >= b[0][0] :
            b[0][0] = a[i][j]
            b[1][0] = i+1
            b[1][1] = j+1
        else :
            pass

for k in b :
    print(*k)
