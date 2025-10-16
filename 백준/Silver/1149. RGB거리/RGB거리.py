n = int(input())

color={}
for i in range(n):
    rgb = list(map(int, input().split()))
    color[i+1] = rgb
    
dp = {}
dp[1] = color[1]

for i in range(2,n+1):
    dp[i] = [0, 0, 0]
    dp[i][0] = min(dp[i-1][1]+color[i][0], dp[i-1][2]+ color[i][0])
    dp[i][1] = min(dp[i-1][0]+color[i][1], dp[i-1][2]+ color[i][1])
    dp[i][2] = min(dp[i-1][0]+color[i][2], dp[i-1][1]+ color[i][2])
    
min_cost = min(dp[n])
print(min_cost)