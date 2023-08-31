# arr=[1,1,3,3,5]
# for i in range(len(arr)) :
#     if arr[0] :
#         continue
#     elif arr[i] == arr[i-1] :
#         arr.pop(i-1)
#     print(arr)

def solution(arr):
    a=[arr[0]]
    for i in range(1,len(arr)) :
        if arr[i-1] != arr[i] :
            a.append(arr[i])
    return a

print(solution([1,1,3,3,0,1,1]))