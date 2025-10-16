n = int(input())

# dp 딕셔너리 생성
dp = {}
## 초기값
dp[1] = 0

# 반복문
for i in range(2,n+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 ==0:
        dp[i] = min(dp[i], dp[i//3] + 1)


print(dp.get(n,0))
    
