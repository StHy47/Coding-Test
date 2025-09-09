import sys

l = sys.stdin.readlines()
n = l[0]
l1 = l[1:]
for i in range(len(l1)):
    a, b = map(int, l1[i].split())
    print(a + b)
