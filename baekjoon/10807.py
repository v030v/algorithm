n = int(input())
a = map(int, input().split(""))
tot = 0
v = int(input())
for i in a :
    if i == v :
        tot += 1
print(tot)