def solution(n) :
    cnt = 1
    a = 0
    b = 0
    for i in range(1,9) :
        if n // (10**i) > 0 :
            b = i


    for j in range(b, 0 , -1) :
        if j == 1:
            a += (n % 10 **j)
            a += (n % 10**(j+1)) // 10 ** j
        elif j > 0 :
            if (n // 10 ** j) >= 10 :
                print((n % 10**(j+1)) // 10 ** j)
                a += (n % 10**(j+1)) // 10 ** j
            else :
                print((n // 10 ** j))
                a += (n // 10 ** j)

    print()
    return a
        
# 실행문
print(solution(588324))