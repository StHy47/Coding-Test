def solution(answers):
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    pro = 0
    
    solve = [0,0,0]
    while pro < len(answers):
        n1 = pro % len(p1)
        if p1[n1] == answers[pro]:
            solve[0] += 1
        n2 = pro % len(p2)
        if p2[n2] == answers[pro]:
            solve[1] += 1
        n3 = pro % len(p3)
        if p3[n3] == answers[pro]:
            solve[2] += 1
        
        pro += 1
    
    
    ### 정답자
    answer = []
    for i in range(len(solve)):
        if solve[i] == max(solve):
            answer.append(i+1)
    return answer