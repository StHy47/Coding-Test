N = int(input())
l = map(int, input().split())
l = list(l)
v = int(input())

n = 0
for i in range(N):
    if v == l[i]:
        n += 1
print(n)
    