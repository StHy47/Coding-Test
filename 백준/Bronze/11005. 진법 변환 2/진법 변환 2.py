num, b = map(int, input().split())
list1= []

while num > 0:
    r = num % b
    if r > 9:
        r = chr(r+55).upper()
    list1.append(r)
    num = int(num/b)
    
    
list1.reverse()

print(*list1, sep='')
