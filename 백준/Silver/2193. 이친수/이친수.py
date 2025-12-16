import sys

n = int(sys.stdin.readline())

# dp[i][0]: i자리이면서 0으로 끝남
# dp[i][1]: i자리이면서 1로 끝남
dp = [[0] * 2 for _ in range(n + 1)]

# 초기값: 1자리 이친수는 무조건 '1' 하나뿐임 (0으로 시작 불가)
dp[1][0] = 0
dp[1][1] = 1

for i in range(2, n + 1):
    # 0으로 끝나는 경우: 앞이 0이든 1이든 상관 없음
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    # 1로 끝나는 경우: 앞이 무조건 0이어야 함
    dp[i][1] = dp[i-1][0]

print(sum(dp[n]))