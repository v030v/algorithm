def solution(a, b):
    answer = 0
    if a > b :
        for i in range(b, a+1) :
            answer += i
    elif a == b :
        return a
    else :
        for i in range(a, b+1) :
            answer += i
    return answer

c = solution(3,5)
print(c)