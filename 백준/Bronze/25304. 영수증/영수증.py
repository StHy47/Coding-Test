price = int(input())
cnt = int(input())

list1 = []
while True:
    try :
        p, c = map(int, input().split())
        if not p:
            break
        list1.append((p,c))
    except Exception as e:
        break


total = 0

for i in range(len(list1)):
    buy = list1[i][0] * list1[i][1]
    total += buy

if price == total:
    print('Yes')
else:
    print('No')