word = input()
n = len(word)
mid = int(n/2)
if n%2 == 1:
    uplist = word[:mid]
    downlist = word[mid+1:]
else:
    uplist = word[:mid]
    downlist = word[mid:]

r_d = list(reversed(downlist))

answer = []
for i in range(len(uplist)):
    if uplist[i] == r_d[i]:
        answer.append('y')
    else:
        answer.append('n')

if 'n' in answer:
    s = 0
else :
    s = 1
print(s)