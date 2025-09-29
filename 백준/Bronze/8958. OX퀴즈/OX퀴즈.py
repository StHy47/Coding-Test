n = int(input())


for _ in range(n):
    a = input()
    pl = 1
    if a[0] == 'O':
        score = 1
    else:
        score =0
    for i in range(1,len(a)):
        if a[i] == 'O':
            if a[i-1] == 'O':
                pl += 1
            else:
                pl = 1
            score += pl
        else:
            pl = 0
    print(score)