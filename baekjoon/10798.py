s = [list(input()) for _ in range(5)]
Maxlen = 0 

for i in range(5) :
    if Maxlen < len(s[i]) :
        Maxlen = len(s[i])
    
for j in range(Maxlen) :
    for i in range(len(s)) :
        if j < len(s[i]) :
            print(s[i][j], end='')
        else :
            pass