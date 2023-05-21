ls = [1, 1, 2, 2, 2, 8]
wh = list(map(int, input().split(" ")))

for i in range(len(ls)) :
    wh[i] = ls[i] - wh[i]
print(*wh)