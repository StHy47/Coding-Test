import sys
input = sys.stdin.readline
n  = int(input())

stack = []

for _ in range(n):
    m = int(input())
    
    if m != 0:
        stack.append(m)
    else:
        stack.pop()
        
print(sum(stack))
   