'''
오늘 날짜 0000.00.00: today
유효기간 약관 배열 : terms
    약관종류(알파벳 대문자) 유효기간(달 수)
    모든 달은 28일 까지 있다고 가정
개인정보 배열 : privacies
    날짜(0000.00.00) 약관종류(알파벳 대문자)
- 파기할 정보를 오름차순으로 1차원 정수 배열로 return

아이디어 : 개인정보를 보고 약관 종류에서 찾아서 해당개월수 만큼 더해서 파기 시점 구하기
'''
def solution(today, terms, privacies):
    answer = []
    # today를 숫자로 변환
    t_y, t_m, t_d = map(int, today.split('.'))
    today = (t_y * 12 * 28) + (t_m * 28) + t_d
    # 계약 별로 분해
    for i in range(len(privacies)):
        p_day, p_type = privacies[i].split()
        
        m = 0   # 계약 개월수 변수 생성
        # 계약 타입을 terms에서 찾기
        for j in range(len(terms)):
            al, mth = terms[j].split() #al = 약관종류, mth = 개월수
            if al == p_type:
                m = int(mth)
        
        # 계약 만료일 : 개인정보의 날짜를 계약월 만큼 더하기
        p_y, p_m, p_d = map(int, p_day.split('.'))
        end_day = (p_y*12*28) + ((p_m*28)+ m*28) + p_d
        
        ## 계약 만료일이 현재 시점보다 이전이면 제거할 리스트에 추가
        if today >= end_day:
            answer.append(i+1)

    return answer