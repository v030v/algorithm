H , M = map(int, input().split())
if H <= 0 :
    if M >= 45 :
        print(H, M-45)
    elif M <= 44 :
        print(H+23, M+15)
else :
    if M >= 45 :
        print(H, M-45)
    elif M <= 44:
        print(H-1, M+15)