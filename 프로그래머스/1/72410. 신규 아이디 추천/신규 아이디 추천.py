import re
def solution(new_id):
    ## 네오의 아이디 추천 단계
    # 1단계 : 대문자 -> 소문자
    neo_id = new_id.lower()
    
    # 2단계 : 소문자, 숫자, -, _, . 빼고 다 제거
    pattern = r'[^a-z-_.0-9]'
    neo_id = re.sub(pattern, '', neo_id)
    
    # 3단계 : .가 두번 반복되면 하나로 변경
    pattern = r'\.{2,}'
    replace = r'.'    
    neo_id = re.sub(pattern, replace, neo_id)
    
    # 4단계 : .가 처음이나 끝이면 제거
    ### 빈 값인데 인덱스 접근하면 에러 날 수 있으니까 길이 조건 부여
    if len(neo_id) > 0 and neo_id[0] == '.':
        neo_id = neo_id[1:]
    if len(neo_id) > 0 and neo_id[-1] == '.':
        neo_id = neo_id[:-1]
        
    # 5단계 : 빈문자열이면 "a" 대입
    if neo_id == '':
        neo_id = 'a'
        
    # 6단계 : 16이상이면 앞에 15자 까지만 아이디
    if len(neo_id) >= 16:
        neo_id = neo_id[:15]
    # 6-1 단계 : 만약에 마지막이 .이면 제거
    if neo_id[-1] == '.':
        neo_id = neo_id[:-1]
    
    # 7단계 : 2자 이하면 마지막 문자 3이 될때까지 반복 붙이기
    while len(neo_id) <= 2:
        neo_id = neo_id + neo_id[-1]
    
    return neo_id