def solution(s):
    if len(s) % 2 != 0 : #글자 수가 홀수일 때
        return s[len(s)//2]
    else : #글자 수가 짝수일 떄
        return s[(len(s)//2)-1]+s[len(s)//2]
    
print(solution("abcde"))
print(solution("qwer"))