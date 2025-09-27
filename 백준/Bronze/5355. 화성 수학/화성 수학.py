n = int(input())
for _ in range(n):
    case = input().split()
    a = float(case[0])
    for i in range(1,len(case)):
        if case[i] == '@':
            a *= 3
        elif case[i] == '%':
            a += 5
        else:
            a -= 7
    print(f"{a:.2f}")