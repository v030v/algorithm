def solution(x, n):
    answer = []
    if x > 0 :
        for i in range(x,(x*n)+1,x) :
            answer.append(i)
    elif x < 0 :
        for i in range(x,(x*n)-1,x) :
            answer.append(i)
    else :
        for i in range(n) :
            answer.append(x)
    return answer

# 실패1
    # answer = []
    # if x > 0 :
    #     for i in range(x,(x*n)+1,x) :
    #         answer.append(i)
    # elif x < 0 :
    #     for i in range(x,(x*n)-1,x) :
    #         answer.append(i)
    # return answer

# 실패2
    # answer = []
    # if x > 0 :
    #     for i in range(x,(x*n)+1,x) :
    #         answer.append(i)
    # elif x < 0 :
    #     for i in range(x,(x*n)-1,x) :
    #         answer.append(i)
    # else :
    #     answer.append(0)
    # return answer
print(solution(4,5))
print(solution(-4,10))