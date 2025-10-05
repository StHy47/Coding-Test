def solution(s):
    l1 = []
    n = len(s)
    answer  = False
    if s[n-1] == ')' and s[0] == '(':
        for i in range(n):
            if s[i] == '(':
                l1.append('a')
            else:
                if not l1:
                    return answer
                l1.pop()
        if l1 == []:
            answer = True

    return answer