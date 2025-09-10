n = int(input())


for _ in range(n):
    num, word = input().split()
    num  = int(num)
    list1=[]
    for i in range(len(word)):
        list1.append(str(word[i])*num)
    print(*list1, sep='')

