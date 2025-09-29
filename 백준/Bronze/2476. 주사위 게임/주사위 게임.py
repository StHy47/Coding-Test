n = int(input())
list1= []

for _ in range(n):
    a,b,c = map(int, input().split())
    l1 = sorted([a,b,c])
    if a==b and b==c:
        s = 10000 + a*1000
    elif a==b and b!=c:
        s = 1000 + a*100
    elif b==c and a!=b:
        s = 1000 + b*100
    elif a==c and a!=b:
        s = 1000 + a*100
    else:
        s = l1[2] * 100
    list1.append(s)
    
print(max(list1))