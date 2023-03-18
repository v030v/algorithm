def solution(n):
    for i in range (1, n+1) :
        if (n // i) == i and n % i == 0 :
            return ((i+1) ** 2)
    return -1
        
print(solution(9856148))