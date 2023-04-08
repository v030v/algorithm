# b = []
# for i in range (10) :
#     a = int(input())
#     if (a % 42) not in b :
#         b.append(a % 42)
# print(len(b))

b = set()
for i in range(10) :
    a = int(input())
    b.add(a%42)
print(len(b))