def solution(progresses, speeds):
    work_days = []
    for i in range(len(speeds)):
        work = progresses[i]
        days = 0
        while work < 100:
            days += 1
            work += speeds[i]
        work_days.append(days)
    
    # 배포 날짜
    answer = []
    cnt = 0
    max_day = work_days[0] # 첫째날
    
    for j in work_days:
        if j <= max_day:
            cnt += 1
        else:
            answer.append(cnt)
            max_day = j
            cnt = 1
    if cnt>0:
        answer.append(cnt)
    
    return answer
            
