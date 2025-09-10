word = input().upper()

dic = {}
for i in word:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] = dic[i] + 1 


answer = []        
for key, value in dic.items():
    if value == max(dic.values()):
        answer.append(key)
    else:
        pass
    
    
if len(answer) == 1:
    print(*answer)
else:
    print('?')
