def solution(N, number):
    ### 값을 저장할 dp캐시 
    dp = {}
    answer = 9
    ## 1~8단계
    for n in range(1,9):
        ### 값이 자기 자신일 때
        dp[n] = set([int(str(N)*n)])
        ### 연산 가능 (1보다 클 때)
        if n > 1:
            for j in range(1,n):
                for k in dp[j]:
                    for l in dp[n-j]:
                        dp[n].add(k+l)
                        dp[n].add(k-l)
                        dp[n].add(k*l)
                        if l != 0:
                            dp[n].add(k // l)
        ###만약 해당 값이 dp[n]에 있으면 그 단계가 정답
        if number in dp[n] and answer > n:
            answer = n
    
    if answer < 9:
        return answer
    else:
        return -1