n,k,m = map(int, input().split())

if n * k > m:
    print(n*k - m)
else:
    print(0)