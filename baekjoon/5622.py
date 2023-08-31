s = input()
ls = list(s)
tm = 0

for i in ls :
    if ord(i) >= 87 :
        tm += 10
    elif ord(i) >= 84 :
        tm += 9
    elif ord(i) >= 80 :
        tm += 8
    elif ord(i) >= 77 :
        tm += 7
    elif ord(i) >= 74 :
        tm += 6
    elif ord(i) >= 71 :
        tm += 5
    elif ord(i) >= 68 :
        tm += 4
    else :
        tm += 3

print(tm)