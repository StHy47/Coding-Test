import math
n = int(input())


for _ in range(n):
    n,m = map(int, input().split())
    answer = math.comb(m, n)
    print(answer)