n , m = map(int, input().split(" "))
e = []
for x in range(n) :
    e.append(0)

for y in range(1, m+1) :
    i, j, k = map(int, input().split(" "))
    for z in range(i-1,j) :
        e[z] = k
print(*e)