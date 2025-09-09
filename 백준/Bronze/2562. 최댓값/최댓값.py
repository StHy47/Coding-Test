import sys

l = []
for i in range(9):
    a = int(input())
    l.append(a)

print(max(l), l.index(max(l))+1, sep ='\n')