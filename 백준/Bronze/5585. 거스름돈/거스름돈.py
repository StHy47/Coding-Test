n = 1000 - int(input())

money = [500, 100, 50, 10, 5, 1]
answer = 0

for i in money:
    k = n // i
    answer += k
    
    n = n % i

print(answer)