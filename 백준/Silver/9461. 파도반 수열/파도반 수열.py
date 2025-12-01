import sys
input = sys.stdin.readline
T = int(input())


dp = {}
dp[1] = 1
dp[2] = 1
dp[3] = 1

for _ in range(T):
    n = int(input())
    
    for i in range(3,n+1):
        if i not in dp:
            dp[i] = dp[i-3] + dp[i-2]
    
    print(dp[n])