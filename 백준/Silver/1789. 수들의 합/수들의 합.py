n = int(input())
cnt = 0
i = 0

while True:
    if n - i >0:
        i += 1
        n = n-i
        cnt += 1
    else :
        break

print(cnt)