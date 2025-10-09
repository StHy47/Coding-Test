def solution(n, info):
    ryan = [0] * 11     # 라이언 빈 화살 리스트
    best_score = 0  ### 최고 점수차 
    best_ryan = [-1]    ### 최고 점수차일 때 라이언의 화살 리스트 : 문제에서 이길 수 없는 경우 -1이므로 디폴트 값은 -1

    # 인덱스, 남은 화살, 현재 상태
    stack = [(0, n, [0]*11)]

    while stack:    # 스택 값이 빌 때까지 반복
        idx, left, now = stack.pop()

        # 11칸 다 하면 점수 계산
        if idx == 11:
            # 만약에 화살이 남으면 남은건 다 0에다가 쏘기(문제에서 가장 낮은 점수를 더 많이 맞힌 경우가 정답)
            if left > 0:    
                now[10] += left     # now[10] : 0점
            
            # 라이언 점수, 어피치 점수 초기화
            r_score, a_score = 0, 0
            
            for i in range(11):
                ## i번째 원의 점수
                score = 10 - i
                # 둘 다 쏜 횟수가 0인 경우에는 아무도 해당 원의 점수를 안 가져가니까 패스
                if now[i] == 0 and info[i] == 0:
                    continue
                # 라이언이 쏜 값이 어피치 값보다 크면 해당 원의 점수는 라이언이 가져감
                if now[i] > info[i]:
                    r_score += score
                # 어피치가 더 많이 쏘거나 동점이면 해당 원의 점수는 어피치가 가져감
                else:
                    a_score += score
            
            ## 라이언과 어피치 총 점수의 차
            diff = r_score - a_score
            
            # 점수차가 0보다 작으면 이길 수 없음 -> 초기 값인 -1 반환
            ## 점수차가 0보다 크면 이길 수 있음
            if diff > 0:
                ## 해당 점수차와 배열로 갱신
                # 1. 점수차가 현재의 최고점수차보다 크거나(문제에서 점수차가 가장 큰 경우가 정답)
                # 2. 점수차가 현재 점수차랑 같다면 더 낮은 점수를 많이 맞힌 리스트가 정답임 - 뒤집어서 비교(점수가 역순이니까)
                if diff > best_score or (diff == best_score and now[::-1] > best_ryan[::-1]):
                    best_score = diff
                    best_ryan = now[:]

            # 초기화
            if left > 0:
                now[10] -= left
            continue

        # 라이언이 이길 수 있음
        need = info[idx] + 1 #라이언이 이기기 위해 해당 점수에 쏴야하는 화살 수
        if left >= need:
            ryan_shoot = now[:]   # 참조를 위한 복사본
            ryan_shoot[idx] = need
            stack.append((idx + 1, left - need, ryan_shoot))

        # 라이언이 이길 수 없는 경우 포기 : -1 반환
        ryan_shoot = now[:]
        stack.append((idx + 1, left, ryan_shoot))

    return best_ryan if best_ryan != [-1] else [-1]
