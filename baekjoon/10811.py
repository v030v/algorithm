n, m = map(int,input().split(" "))
b = []
for x in range(1, n+1) :
    b.append(x) 
for _ in range(m) :
    i,j = map(int, input().split(" "))
#     if j-i == 1 :
#         b[(i-1)], b[(i+j-2)-(i-1)] = b[(i+j-2)-(i-1)], b[(i-1)]
#     else :
#         for y in range((i-1), ((i+j)//2)) :
#             b[y], b[(i+j-2)-y] = b[(i+j-2)-y], b[y]
# print(*b)
    
# 2    
#     for y in range(i-1, (i+j)//2) :
#         b[y], b[(i+j-2)-y] = b[(i+j-2)-y], b[y]
# print(*b)

# other
    b[i-1:j] = b[i-1:j][::-1]
print(*b)