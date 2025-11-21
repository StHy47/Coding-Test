import sys
input = sys.stdin.readline
T = int(input())
stack = []
for _ in range(T):
    i = input().rstrip()
    if i.startswith('push'):
        cmd, x = i.split()
        stack.append(int(x))
    elif i == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif i == 'size':
        print(len(stack))
    elif i =='empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])