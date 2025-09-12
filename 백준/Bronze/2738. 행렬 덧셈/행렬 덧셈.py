N, M = map(int, input().split())
a = []
b = []

for i in range(N):
    x = list(input().split())
    a.append(x)
    
for i in range(N):
    y = list(input().split())
    b.append(y)
    
answer = []
    
for i in range(N):
    list1 = []
    for j in range(M):
        k = int(a[i][j]) + int(b[i][j])
        list1.append(k)
    answer.append(list1)
    
    
for i in answer:
    print(*i)
        
        
 