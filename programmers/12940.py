def solution(n, m):
    answer = []
    j = 1
    if n > m :
        n,m = m,n
    for i in range(2,m+1) :
        if n % i == 0 and m % i == 0 :
            j *= i
            n = (n // i)
            m = (m // i)
            while n % i == 0 and m % i == 0 :
                j *= i
                n = (n // i)
                m = (m // i)
    answer.append(j)
    answer.append(j*n*m)
    return answer

print(solution(24,56))

# # 복습1
# import math
# math.gcd(a,b)
# math.lcm(a,b)

# # 복습2
# 유클리드 호제법
# 최소공배수 = (a*b)/최대공약수
# 최대공약수 = a/b = r...?