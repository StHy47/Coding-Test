n = int(input())
km = list(map(int,input().split()))
city = list(map(int, input().split()))

money = city[0]*km[0] ### 초기 비용 : 첫번째 도시에서 다음 도시로 가기 위해서는 무조건 주유해야함
min_city = city[0]

for i in range(1,len(city)-1):
        min_city = min(city[i], min_city)
        price = min_city * km[i]
        money += price
        
print(money)
        
            