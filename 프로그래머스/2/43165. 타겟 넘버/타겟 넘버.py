def solution(numbers, target):
    answer = 0

    def dfs(i, current_sum):
        nonlocal answer  # global 대신 이렇게!
        
        # 모든 숫자 다 썼을 때
        if i == len(numbers):
            if current_sum == target:
                answer += 1
            return

        # + 선택
        dfs(i + 1, current_sum + numbers[i])
        # - 선택
        dfs(i + 1, current_sum - numbers[i])


    dfs(0,0)
        
        
    return answer

