n = int(input())

### 세로 : 1 / 가로2개
### n을 1,2로 구성

dp = {}
dp[1] = 1
dp[2] = 2

for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-2]
    
print(dp[n]%10007)