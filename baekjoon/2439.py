n = int(input())
i = 0
while i < n :
    j = 0
    while j < n :
        if i+j >= (n-1) :
            print('*', end = "")
        else :
            print(' ', end = "")
        j += 1
    i += 1
    print()

# i = 1
# while i <= n :
#     print(' '*(n-i)+'*'*i)
#     i += 1