n = int(input())
for _ in range(n):
    list1 = list(input())
    
    stack = []
    answer = 'YES'
    
    for i in range(len(list1)):
        if i == 0 and list1[i] == ')':
            answer = 'NO'
            break
            
        if list1[i] == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                answer = 'NO'
                break
            else:
                stack.pop()
    if len(stack) > 0:
        answer = 'NO'

    print(answer)