n = int(input())
cnt_0 = 0
cnt_1 = 0

for _ in range(n):
    a = int(input())
    if a == 0:
        cnt_0 += 1
    else:
        cnt_1 += 1

if cnt_0 > cnt_1:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')