t = int(input())
floor = {}
floor[0] = [i for i in range(1,15)] # 각 층은 14호 까지 있음
for _ in range(t):
    k = int(input())
    n = int(input())

    for j in range(1,k+1):
        if j not in floor:
            floor[j] = [sum(floor[j-1][0:i]) for i in range(1,15)]
            
    print(floor[k][n-1])
    