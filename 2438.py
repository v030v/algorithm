n = int(input())
for i in range(1,n+1) :
    for j in range(i) :
        print('*',end="")
    print()

# n = int(input())
# for i in range(n) :
#     for j in range(i+1) :
#         print('*',end="")
#     print()

n = int(input())
for i in range(n) :
    print('*' * (i+1)) 
print()