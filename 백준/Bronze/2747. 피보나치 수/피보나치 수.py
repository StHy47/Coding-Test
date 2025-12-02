n = int(input())
f = {}
f[0] = 0
f[1] = 1
f[2] = 1
for i in range(2,n+1):
    f[i] = f[i-2] + f[i-1]
    
print(f[n])