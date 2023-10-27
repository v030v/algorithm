t = int(input())
for i in range(t) :
    c = int(input())
    cls = []
    cls.append(c//25)
    cls.append((c%25)//10)
    cls. append(((c%25)%10)//5)
    cls.append((((c%25)%10)%5)//1)
    
    print(*cls)
          