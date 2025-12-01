import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B, reverse = True)

answer = 0
for i in range(n):
    n = A[i]*B[i]
    answer += n
    
print(answer)