# n = int(input())
# data = list(map(int, input().split(' ')))
# print(min(data), max(data))

n = int(input())
data = list(map(int, input().split(' ')))
mx = data[0]
mn = data[0]
for i in range(1, len(data)) :
    if mx < data[i] :
        mx = data[i]
    if mn > data[i] :
        mn = data [i]
print(mx, mn)
