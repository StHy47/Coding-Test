def solution(triangle):
    dp = {}
    dp[0] = triangle[0]
    lv = len(triangle) ## 트리 깊이
    
    if lv > 0:
        dp[1] = [dp[0][0]+triangle[1][0], dp[0][0]+triangle[1][1]]
    
    if lv > 2:
        for i in range(2,lv):
            dp[i] = []
            # j는 0부터 i까지 (현재 층의 원소 개수만큼) 돌아야 합니다.
            for j in range(i + 1): 
            
                # 1. 맨 왼쪽 (j == 0)일 때
                if j == 0:
                    value = dp[i-1][0] + triangle[i][0]
            
             # 2. 맨 오른쪽 (j == i)일 때
                elif j == i:
                    value = dp[i-1][j-1] + triangle[i][j]
                
                # 3. 가운데 (0 < j < i)일 때
                else:
                    left_parent = dp[i-1][j-1]
                    right_parent = dp[i-1][j]
                    value = max(left_parent, right_parent) + triangle[i][j]
                
                # 계산된 값을 현재 층 dp[i]에 추가
                dp[i].append(value)
                
    answer = max(dp[lv-1])
    return answer