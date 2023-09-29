w = [[0]*101 for _ in range(101)]
t = int(input())
count = 0

for i in range(t) :
    c,p = map(int, input().split())
    for j in range(c,c+10) :
        for k in range(p,p+10) :
            if w[k][j] == 1 :
                pass
            else :
                w[k][j] = 1

# for l in range(1,101) :
#     for m in range(1,101):
#         if w[l][m] == 0 :
#             count += 1
#         else :
#             pass

tot = sum(w,[])

print(sum(tot))