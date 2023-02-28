def solution(x, n):
    answer = []
    if x > 0 :
        for i in range(x,(x*n)+1,x) :
            answer.append(i)
    elif x < 0 :
        for i in range(x,(x*n)-1,x) :
            answer.append(i)
    return answer

print(solution(4,5))
print(solution(-4,10))