l1 = []
for _ in range(3):
    list1 = list(input().split())
    l1.append(list1)
    
x =[]
y =[]

for i in range(3):
    if l1[i][0] in x:
        x.remove(l1[i][0])
    else:
        x.append(l1[i][0])
        
    if l1[i][1] in y:
        y.remove(l1[i][1])
    else:
        y.append(l1[i][1])
        
print(*x)
print(*y)
        