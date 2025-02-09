import sys
n = int(input())
r = list(map(int, sys.stdin.readline().split(" ")))
tot = 0
i = 0

while i < n :
    if i+1 > n-1 and i+2 > n-1:
        if r[i] >= 1 :
            tot += r[i]*3
            r[i] = 0
            
    elif i < n-2 and r[i] >= 1 and r[i+1] >= 1 and r[i+2] >= 1 :
        tot += 7
        r[i] -= 1
        r[i+1] -= 1
        r[i+2] -= 1
        if r[i] > 0 :
            while r[i] != 0 :
                if r[i+1] == 0 :
                    tot += r[i]*3
                    r[i] = 0
                elif r[i+2] == 0 :
                    while r[i] != 0 :
                        if r[i+1] > 0 :
                            tot += 5
                            r[i] -= 1
                            r[i+1] -= 1
                        elif r[i+1] == 0 :
                            tot += r[i]*3
                            r[i] = 0
                else :
                    tot += 7
                    r[i] -= 1
                    r[i+1] -= 1
                    r[i+2] -= 1

    elif r[i] >= 1 and r[i+1] >= 1 :
        tot += 5
        r[i] -= 1
        r[i+1] -= 1
        if r[i] > 0 :
            while r[i] != 0 :
                if r[i+1] == 0 :
                    tot += (r[i]*3)
                    r[i] = 0
                else :
                    while r[i] != 0 :
                        tot += 5
                        r[i] -= 1
                        r[i+1] -= 1
                   
    elif r[i] >= 1 :
        tot += (r[i]*3)

    i += 1

print(tot)