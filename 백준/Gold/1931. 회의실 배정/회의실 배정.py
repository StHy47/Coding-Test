import sys
input = sys.stdin.readline

n = int(input())

### 시간 입력
time = []
for _ in range(n):
    a  = list(map(int, input().split()))
    time.append(a)
time.sort(key=lambda x : (x[1], x[0])) ### 끝나는 시간 - 시작 시간 기준 정렬

### 끝나는 시간이랑 비교해서 가장 짧은 시간 선택
end, cnt = 0, 0
for i in range(n):
    if time[i][0] >= end:
            end = time[i][1]
            cnt += 1

print(cnt)
            
            