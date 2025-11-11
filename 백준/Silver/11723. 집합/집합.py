import sys
input = sys.stdin.readline

N = int(input())
S = set()

for _ in range(N):
    cmd = input().strip().split()
    do = cmd[0]
    
    if do == 'all':
        S = set(x for x in range(1,21))
    elif do == 'empty':
        S = set()
    else:
        x = int(cmd[1])
        if do == 'add':
            S.add(x)
        elif do == 'remove':
            S.discard(x)
        elif do == 'toggle':
            if x not in S:
                S.add(x)
            else:
                S.discard(x)
        else:
            print(1 if x in S else 0)