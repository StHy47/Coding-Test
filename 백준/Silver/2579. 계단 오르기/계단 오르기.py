t = int(input())

score = {}
for i in range(1, t + 1):
    score[i] = int(input())

if t == 1:
    print(score[1])
else:
    dp = {}
    dp[1] = score[1]
    dp[2] = score[1] + score[2]
    
    for i in range(3, t + 1):
        dp[i] = max(dp.get(i-2, 0) + score[i], dp.get(i-3, 0) + score[i-1] + score[i])

    print(dp[t])

