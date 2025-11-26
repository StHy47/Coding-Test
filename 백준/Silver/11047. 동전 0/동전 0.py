import sys
input = sys.stdin.readline

num = []
n, k = map(int, input().split())
for _ in range(n):
    i = int(input())
    num.append(i)
    
num.reverse()
money = 0
for i in num:
    r = k // i
    k = k % i
    money += r
    
print(money)