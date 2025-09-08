a,b,c = map(int, input().split())
l1 = sorted([a,b,c])


if l1[0] == l1[1] and l1[0] == l1[2]:
    p = 10000 + l1[0]* 1000
elif l1[0] == l1[1] and l1[0] != l1[2]:
    p = 1000 + l1[0]*100
elif l1[0] == l1[2] and l1[0] != l1[1]:
    p = 1000 + l1[0]*100
elif l1[1] == l1[2] and l1[0] != l1[1]:
    p = 1000 + l1[1] *100
else:
    p = l1[2] * 100

print(p)