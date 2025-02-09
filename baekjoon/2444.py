n = int(input())
s = 1
for i in range(1, 2*N) :
    if s==1 :
        print('*'*s)
        s += 2
    elif s+2 < 2*n-1 :
        print('*'* s+2)
       