n = int(input())
m = list(map(int,input().split()))
M = max(m)
tot = 0
for i in range(len(m)) :
    m[i] = m[i]/M*100
    tot += m[i]
print(tot/n)

# other 1
# print(sum(m)/max(m)*100/n)