n, m = map(int, input().split())

l = list(range(1,n+1))

for _ in range(m):
    a,b = map(int, input().split())
    l[a-1:b] = list(reversed(l[a-1:b])) 
    
print(*l)