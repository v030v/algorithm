# lst =[]
# i = 1
# while i < 10 :
#     n = int(input())
#     lst.append(n)
#     i += 1
# print(max(lst), lst.index(max(lst))+1)

lst = [1,21,35,-4,5]
mx = lst[0]
for i in range(1, len(lst)) :
    if mx < lst[i] :
        mx = lst[i]
print(mx)

