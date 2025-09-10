a,b = map(int, input().split())

x = ''.join(reversed(list(str(a))))
y = ''.join(reversed(list(str(b))))

if x >= y:
    print(x)
else:
    print(y)