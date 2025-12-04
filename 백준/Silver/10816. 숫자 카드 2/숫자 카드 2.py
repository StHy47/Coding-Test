## 값 입력
from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

num_counts = Counter(num)

answer = []
for i in m_list:
    answer.append(num_counts.get(i, 0))
                
                
print(*answer)

