import math
### 숫자 입력 받기
m = int(input())
n = int(input())
### 범위 내 자연수
a = math.ceil(m**(1/2))
b = int(n**(1/2))


### 완전 수 리스트
num_list = []
if a <= b:
    for i in range(a,b+1):
        num_list.append(i**2)

if sum(num_list) == 0:
    print(-1)
else:
    print(sum(num_list))
    print(min(num_list))