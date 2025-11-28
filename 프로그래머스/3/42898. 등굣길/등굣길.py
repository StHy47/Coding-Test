def solution(m, n, puddles):
    ### 빈 값 생성
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    dp[1][1] = 1
    
    ### 못지나가는 경로 제외
    for x,y in puddles:
        dp[x][y] = -1
    
    for i in range(1,m+1):
        for j in range(1, n+1):
            ### 만약 웅덩이면 건너뛰기
            if dp[i][j] == -1 or (i==1 and j==1):
                pass
            ## 경로
            else:
                if dp[i-1][j] == -1:
                    dp[i][j] = dp[i][j-1]
                elif dp[i][j-1] == -1:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
            
                
    answer = dp[m][n]
    return answer % 1000000007