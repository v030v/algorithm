x = []
for i in range(1, 31) :
    x.append(i)
for j in range(28) :
    m = int(input())
    if m in x :
        x.remove(m)
print(*x, sep="\n")

# 비트연산자