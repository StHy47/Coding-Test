import re
num = input()
num = re.split(r'([-+])', num)

## 숫자형으로 바꿔주기
for i in range(len(num)):
    try:
        n = int(num[i])
        num[i] = n
    except Exception as e:
        pass
    
### 1. 더하기 연산 먼저 처리
while True:
    try:
        i = num.index('+')
        num[i-1:i+2] = [num[i-1]+num[i+1]]
    except Exception as e:
        break
### 2. 빼기 연산 처리                
while True:
    try:
        i = num.index('-')
        num[i-1:i+2] = [num[i-1]-num[i+1]]
    except Exception as e:
        break
print(*num)