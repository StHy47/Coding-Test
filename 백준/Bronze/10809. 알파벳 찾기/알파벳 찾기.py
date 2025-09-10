word = list(input().lower())
l1 = [chr(c).lower() for c in range(ord('A'),ord('Z')+1)]

for i in range(len(word)):
    for j in range(len(l1)):
        if word[i] == l1[j] and type(l1[j]) != int:
            l1[j] = i

answer = []            
for i in range(len(l1)):
    if type(l1[i]) == str:
        answer.append(-1)
    else:
        answer.append(l1[i])
        
print(*answer)
        
        
        
        
