num, b = input().split()
num = str(num)
b = int(b)
a = 0
n = len(num)

for i in range(n):
    try :
        k = int(num[i])
    except Exception as e:
        k = ord(num[i]) - 55
    a += (b**(n-i-1)) * k
    
print(a)