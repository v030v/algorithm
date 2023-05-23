s = input()
# asc = []

# # case 1
# for i in range (97,123) :
#     asc.append(chr(i))
# for j in range(len(asc)) :
#     if asc[j-1] in s :
#         asc[j-1] = s.index(asc[j-1])
#     else :
#         asc[j-1] = -1
# print (*asc)

# # case 2
# for k in range(97, 123) :
#     if chr(k) in s :
#         asc.append(s.index(chr(k)))
#     else :
#         asc.append(-1)
# print(*asc)

# case 3
asc = [-1 for i in range(26)]
for j in range (len(s)) :
    if asc[ord(s[j])-97] < 0 :
        asc[ord(s[j])-97] = j
print(*asc)
