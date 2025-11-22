## 문제 풀이 아이디어 : dp에 계산한 값을 추가로 더해주며 누적합과 현재 값 비교
n = int(input())
num = list(map(int, input().split()))

dp = [0]*n
dp[0] = num[0]

for i in range(1, n):
    dp[i] = max(num[i], dp[i-1]+num[i])
    
print(max(dp))
    

#### 처음 풀이 - 시간초과 : for 문을 이중으로 써서 시간 복잡도가 큼
'''
n = int(input())
num = list(map(int, input().split()))

dp = {} ## 선택 갯수 i - dp[i] = [#선택 가능한 값 리스트]

for i in range(1,n+1):    #선택할 수 갯수
    dp[i] = 0
    for j in range(n):
        n_sum = sum(num[j:j+i])
        if n_sum > dp[i]:
            dp[i] = n_sum
            
print(max(dp.values))

'''


        
        
    

    
