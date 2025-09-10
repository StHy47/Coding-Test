n = int(input())

for i in range(1,n):
    print(' '*(n-i),'*'*(2*i-1), sep='')

for j in range(n+1):
    print(' '*j, '*'*(2*(n-j)-1), sep='')
