while True:
    a = int(input())
    if a == -1:
        break
        
    l1 = []
    for i in range(1,a+1):
        if a % i == 0:
            l1.append(i)
    l1.remove(a)
    if a == sum(l1):
        s = ' + '.join(map(str, l1))
        print(f"{a} = {s}")
    else:
        print(f'{a} is NOT perfect.')