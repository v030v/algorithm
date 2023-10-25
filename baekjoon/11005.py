n, b = map(int, input().split())
ls = []
dic = {}
j = 10

for i in range (65, 91) :
    dic[j] = chr(i)
    j += 1

while n != 0 :
    if n%b >= 10 :
        ls.append(dic[n%b])
    else :
        ls.append(n%b)
    n = n // b
    

print("".join(map(str, ls[::-1])))
