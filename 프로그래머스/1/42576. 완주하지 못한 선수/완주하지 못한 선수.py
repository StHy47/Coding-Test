def solution(participant, completion):
    participant.sort()  # participant 리스트 정렬
    completion.sort()    # completion 리스트 정렬
    
    # 정렬된 리스트를 비교하면서 다르면 해당 값을 반환
    for p, c in zip(participant, completion):
        if p != c:
            return p
    
    # 모든 값이 같으면 마지막 participant가 답
    return participant[-1]
