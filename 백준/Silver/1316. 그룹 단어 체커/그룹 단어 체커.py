n = int(input())
list1 = []
for _ in range(n):
    word = input()
    word_list = []
    for i in range(len(word)):
        if i == 0:
            word_list.append(word[0])
        else:
            if word[i-1] == word[i]:
                pass
            else :
                word_list.append(word[i])
    n = "".join(word_list)
    list1.append(n)


cnt = 0        
for i in range(len(list1)):
    if len(list1[i]) == len(set(list1[i])):
        cnt += 1
    else : 
        pass

print(cnt)