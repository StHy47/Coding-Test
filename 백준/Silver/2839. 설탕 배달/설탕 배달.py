n = int(input())


dp = [-1] * (n + 1) 
dp[0] = 0 


for i in range(1, n + 1):
    res_3 = dp[i-3] if i >= 3 else -1
    res_5 = dp[i-5] if i >= 5 else -1

    if res_3 == -1 and res_5 == -1:
        dp[i] = -1
    elif res_3 != -1 and res_5 == -1:
        dp[i] = 1 + res_3
    elif res_3 == -1 and res_5 != -1:
        dp[i] = 1 + res_5
    else:
        dp[i] = 1 + min(res_3, res_5)

print(dp[n])