case = int(input())

for _ in range(case):
    n = int(input())
    dic = {}
    for _ in range(n):
        sch, l = input().split()
        l = int(l)
        dic[sch] = l
    ml = max(dic.values())
    
    for sch, l in dic.items():
        if l == ml:
            print(sch)