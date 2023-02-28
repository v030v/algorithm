A, B = map(int, input().split())
C = int(input())
tot = A * 60 + B + C
if tot >= 1440 :
    tot -= 1440
A = tot // 60
B = tot % 60
print (A, B)