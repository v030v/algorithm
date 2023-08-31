def solution(num):
    if num % 2 == 0 or num == 0 :
        return "Even"
    else :
        return "Odd"
    
# 다른 이의 풀이
# 1 def solution(num): return ["Even", "Odd"].pop(num % 2)
# 2 def evenOrOdd(num): return ["Even", "Odd"][num & 1]

# 실행문
print(solution(3))
print(solution(4))