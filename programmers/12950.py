def solution(arr1, arr2):
    a = [[0 for j in range(len(arr1[0]))] for i in range(len(arr1))]
    for i in range (len(arr1)) :
        for j in range(len(arr1[0])) :
             a[i][j] = arr1[i][j] + arr2[i][j]
    return a

# 실행문
print(solution([[1,2],[2,3]],[[3,4],[5,6]]))
print(solution([[1],[2]],[[3],[4]]))