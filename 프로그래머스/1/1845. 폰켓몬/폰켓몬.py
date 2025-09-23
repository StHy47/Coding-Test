def solution(nums):
    pm = set(nums)
    n = len(nums)
    if n/2 <= len(pm) :
        answer = n/2
    else:
        answer = len(pm)
    
    
    return answer