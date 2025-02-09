fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']
count = 0

for f in fruits :
    if f == '사과':
        count += 1
    else :
        pass
print(count)
        
        
def count_fruit(fruits_name) :
    fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']
    count = 0
    
    for f in fruits :
        if f == fruits_name :
            count += 1
            
    return count

print(count_fruit('배'))

people = [{'name': 'bob', 'age': 20}, 
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

def get_age(name) :
    for i in range(len(people)) :
        if people[i]['name'] == name :
            return people[i]['age']
        
        else :
            return '정민우바보'

def gett_age(nname) :
    for peorson in people :
        if peorson['name'] == nname :
            return peorson['age']
    return '존재하지 않아'           
            
print(get_age('bob'))
print(get_age('정민우'))
print(gett_age('carry'))
print(gett_age('정민우'))