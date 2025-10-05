from collections import Counter

def solution(clothes):
    category_list = [item[1] for item in clothes]
    counts = Counter(category_list)
    
    answer = 1

    for count in counts.values():
        answer *= (count + 1)
        
    return answer - 1