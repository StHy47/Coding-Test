import sys

n,k = map(int, sys.stdin.readline().split())
z = 0
up = []
for _ in range(n):
    a,b = map(int, sys.stdin.readline().split())
    
    if a < b :
        up.append(b-a)
    else:
        z += 1

if z < k:
    m = k-z
    up = sorted(up)
    x = up[m-1]
else:
    x = 0
        
print(x)