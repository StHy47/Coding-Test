n = int(input())

for _ in range(n):
    g = 1
    x,y = map(int, input().split())
    if x > y:
        a = y
        b = x
    else:
        a = x
        b = y
    for i in range(1,a+1):
        if a % i == 0 and b % i == 0:
            g = i
    k = (a/g) * (b/g) * g
    print(int(k))
        