def solution(n) :
    cnt = 1
    a = 0
    b = 0
    for i in range(1,9) :
        if n // (10**i) > 0 :
            b = i


    for j in range(b, 0 , -1) :
        if j == 1:
            #a += (n % 10 **j)
            a += (n % 10**(j+1)) // 10 ** j
        elif j > 0 :
            if (n // 10 ** j) >= 10 :
                print((n % 10**(j+1)) // 10 ** j)
                a += (n % 10**(j+1)) // 10 ** j
            else :
                print((n // 10 ** j))
                a += (n // 10 ** j)

    a += n % 10
    return a
        
# 실행문
print(solution(35231))



# case 0 정인이 이야기(앞에서부터 더하기 : 35231 >> 3 5 2 3 1) (십의 자리와 일의자리의 합을 한번에 구했다)
# case 1 민우 이야기 : 일의 자리 값을 구할때 더 쉬운 방법이 있었다 ㅋㅋㅋ (line 22)
# case 2 민우 왈 : 숫자의 길이를 구할때 , break의 도움을 받아보자.. 
# case 3 뒤에서 부터 더하기 (35231 >> 1 3 2 5 3)
# case 4 값의 길이를 구할때 문자열의 도움을 받았다
# case 5 그냥 문자열 도움을 받았다

# 진짜 고민 많이하고 풀어본 문제니까 쉬운방법으로만 풀지말고 위의 모든 방법 모두 복습해봐라
