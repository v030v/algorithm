# def palindrom(sentence) :
#     sen = list(sentence)
#     revsen = list(reversed(sen))
#     count = 0
#     for i in range(len(sen)) :
#         if sen[i] == revsen[i] :
#             count += 1
        
#     if count == len(sen) :
#         return 'True'
    
#     else :
#         return 'False'
    
# print(palindrom('radar'))
# print(palindrom('python'))

def palindrom(sentence) :
    for i in range(len(sentence)//2) :
        if sentence[i] != sentence[-i-1] :
            return False
    return True
            
print(palindrom('radar'))
print(palindrom("python"))
print(palindrom("sees"))