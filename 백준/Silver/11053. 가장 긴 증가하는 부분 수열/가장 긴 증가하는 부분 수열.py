n = int(input())
num_list = list(map(int, input().split()))

dp = [1]*n

for i in range(n):
    for j in range(i): ### 앞에서부터 i까지
        if num_list[j] < num_list[i]:
            dp[i] = max(dp[i], dp[j]+1)
            
print(max(dp))
    

