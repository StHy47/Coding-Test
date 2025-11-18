### bottom-up 방식
T = int(input())

tb = [[0,0] for _ in range(41)] ### 40까지 빈 테이블 생성

tb[0] = [1,0]
tb[1] = [0,1]
    
for i in range(2, 41):
    tb[i][0] = tb[i-1][0] + tb[i-2][0]
    tb[i][1] = tb[i-1][1] + tb[i-2][1]

for _ in range(T):
    n = int(input())
    print(tb[n][0], tb[n][1])
        
