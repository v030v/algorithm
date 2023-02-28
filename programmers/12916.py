def solution(s):
    return s.count('p') + s.count('P') == s.count('y') + s.count('Y')
# 2    
    # p = 0
    # y = 0
    # for i in range(len(s)) :
    #     if s[i] == 'p' or s[i] == 'P':
    #         p+= 1
    #     elif s[i] == 'y' or s[i] == 'Y' :
    #         y+= 1
    # if p == y :
    #     return True
    # else :
    #     return False

# 3
    # if s.count('p') + s.count('P') == s.count('y') + s.count('Y') :
    #     return True
    # else :
    #     return False

# 실행 값
print(solution('Pyy'))
print(solution('Pp000yy'))



