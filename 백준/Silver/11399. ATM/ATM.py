n = int(input())
num = sorted(list(map(int,input().split())))
hour = []
for i in range(n):
    hour.append(sum(num[0:i+1]))
    
    
print(sum(hour))