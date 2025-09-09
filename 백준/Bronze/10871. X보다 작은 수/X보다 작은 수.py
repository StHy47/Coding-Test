N, x = map(int, input().split())
l = list(map(int,input().split()))

list1 = []
for i in range(N):
    if l[i] < x:
        list1.append(l[i])

print(*list1)