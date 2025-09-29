dish = input()
high = 10

for i in range(len(dish)-1):
    if dish[i] != dish[i+1]:
        high += 10
    else:
        high += 5
print(high)
    