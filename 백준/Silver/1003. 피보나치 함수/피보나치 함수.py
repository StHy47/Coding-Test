import sys
input = sys.stdin.readline


T = int(input())
dp = {}
dp[0] = [1,0]
dp[1] = [0,1]
    
def fibo(x):
    ## 종료 조건 + dp에 있으면 꺼내기
    if x in dp:
        return dp[x]
    
    ## 재귀
    else:
        x_0 = fibo(x-1)[0] + fibo(x-2)[0]
        x_1 = fibo(x-1)[1] + fibo(x-2)[1]
        dp[x] = [x_0, x_1]
        return dp[x]
    
for _ in range(T):
    n = int(input()) 
    answer = fibo(n)
    print(f"{answer[0]} {answer[1]}")