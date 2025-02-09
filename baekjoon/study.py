#2563
r=range
a=[100*[0]for _ in r(100)]
for i in[*open(0)][1:]:
 x,y=map(int,i.split())
 for i in r(x,x+10):a[i][y:y+10]=[1]*10
print(sum(sum(a[i])for i in r(100)))

a=[0 for _ in range(10000)]
b=int(input())
for _ in range(b):
    N,M=map(int, input().split())
    for _ in range(10):
        for _ in range(10):
            a[N*100+M]=1
            M+=1
        N+=1
        M-=10
print(a.count(1))
