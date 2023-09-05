a=[]
b=[]
c=[]
n, m = map(int, input().split())

# a = [[int(input()) for j in range(m)] for i in range(n)]
# b = [[int(input()) for l in range(m)] for k in range(n)]
a = [list(map(int, input().split())) for i in range(n)]
b = [list(map(int, input().split())) for k in range(n)]
# for i in range(n) :
#     line = []
#     for j in range(m) :
#         line.append(int(input()))
#     a.append(line)

for x in range(len(a)) :
    line = []
    for y in range(len(a[x])) :
        line.append(a[x][y]+b[x][y])
    c.append(line)

for z in c :
    print(*z)
