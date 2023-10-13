n, b = input().split()
tot = 0
dic = {}
j = 10

for i in range (65, 91) :
    dic[chr(i)] = j
    j += 1
    
for k in range (len(n)-1,-1,-1) :
    if n[k] in dic :
        tot += (dic[n[k]] * (int(b)**(len(n)-1-k)))
    else :
        tot += (int(n[k]) * (int(b)**(len(n)-1-k)))
print(tot)
