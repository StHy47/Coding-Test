n = int(input())

for i in range(n):
    m = int(input())
    qt = m // 25
    r = m % 25
    dm = r//10
    r = r % 10
    nk = r // 5
    py = r % 5
    print(qt, dm, nk, py)