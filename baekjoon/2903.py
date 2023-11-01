m = 2
n = int(input())
k = 0
for i in range(n) :
    k = (m+(m-1)) ** 2
    m = (m+(m-1))

print(k)