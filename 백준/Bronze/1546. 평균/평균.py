n = int(input())
score = list(map(int, input().split()))

m = 0
for i in range(n):
    s = score[i]/max(score) * 100
    m += s

print(m/n)