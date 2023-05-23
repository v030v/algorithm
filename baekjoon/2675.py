# case 1
t = int(input())
for i in range(t) :
    r, s = input().split()
    p = []
    for j in range(len(s)) :
        for k in range(int(r)) :
            p.append(s[j])
    print("".join(p))

# # case 2
# t = int(input())
# for i in range(t) :
#     r,s = input().split()
#     p = []
#     for j in range(len(s)) :
#         for k in range(r) :
#             p.append(s[j])
#     print(*p)

# # case 3
# t = int(input())
# for i in range(t) :
#     r, s = input().split()
#     for j in range(len(s)) :
#         for k in range(int(r)) :
#             print(s[j],end='')
#     print()