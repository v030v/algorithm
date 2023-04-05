n, m = map(int, input().split(" "))
k = []
for x in range(n+1) :
    k.append(x)
for y in range(m) :
    i, j = map(int, input().split(" "))
    k[i], k[j] = k[j], k[i]
print(*k[1:n+1])