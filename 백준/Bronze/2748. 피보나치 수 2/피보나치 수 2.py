n = int(input())

f = {}
f[0] = 0
f[1] = 1

for x in range(1, n+2):
    if x in f:
        f[x] = x
    else:
        f[x] = f[x-1] + f[x-2]

print(f[n])