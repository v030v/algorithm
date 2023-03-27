# n = int(input())
# for i in range(1,n+1) :
#     for j in range(i) :
#         print('*',end="")
#     print()

# n = int(input())
# for i in range(n) :
#     for j in range(i+1) :
#         print('*',end="")
#     print()

# n = int(input())
# for i in range(n) :
#     print('*' * (i+1)) 
# print()

# n = int(input())
# i = 1
# while i <= n :
#     print('*'*i)
#     i += 1

n = int(input())
i = 0
while i < n :
    j = 0
    while j < n :
        if i >= j :
            print('*', end = "")
        j += 1
    i += 1
    print()

