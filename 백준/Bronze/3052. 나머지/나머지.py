l=[]
for _ in range(10):
    a = int(input())
    l.append(a%42)


print(len(set(l)))
