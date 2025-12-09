a, b = map(str,input().split())
cnt = 1
num = b
while True:
    if int(a) >= int(num):
        break
    else:
        cnt += 1
        num = str(num)
        if num[-1] == '1':
            num = num[:-1]
        else:
            num = int(num)
            if num % 2 == 0:
                num = num//2
            else:
                break
        

if a == str(num):
    print(cnt)
else:
    print(-1)
        
        
        
        
    