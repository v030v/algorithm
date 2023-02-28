def solution(n) :
    answer = "수박"
    if n % 2 == 1 :
        return answer * ((n-1) // 2) + answer[0]
    return answer * (n // 2)

wm = solution(6)
print(wm)