def solution(commands):
    answer = []
    # 빈 셀 50*50 생성
    cell = [['EMPTY' for _ in range(51)] for _ in range(51)]  
    # 셀 위치 확인용
    check = [[[i, j] for j in range(51)] for i in range(51)]
    
    def insert(r, c, v):
        # check해서 위치 찾기
        c_r, c_c = check[r][c] 
        cell[c_r][c_c] = v
        
    def update(v1, v2):
        for i in range(51):
            for j in range(51):
                if cell[i][j] == v1:
                    cell[i][j] = v2
                    
    def merge(r1, c1, r2, c2):
        c_r1, c_c1 = check[r1][c1]  # 1번 셀의 실제 위치
        c_r2, c_c2 = check[r2][c2]  # 2번 셀의 실제 위치
        value1, value2 = [cell[c_r1][c_c1], cell[c_r2][c_c2]]  # 각 셀 값을 가져옴
        cell[c_r1][c_c1] = value2 if value1 == 'EMPTY' else value1  # 값 변경
        for i in range(51):
            for j in range(51):
                if check[i][j] == [c_r2, c_c2]: # 2번 셀의 포인터를 1번 셀의 위치로 변경
                    check[i][j] = [c_r1, c_c1]  
        
    def unmerge(r, c):
        c_r, c_c = check[r][c]  # 실제 위치 가져옴
        value = cell[c_r][c_c]  # 셀 값 가져옴
        for i in range(51):
            for j in range(51):
                if check[i][j] == [c_r, c_c]:
                    check[i][j] = [i, j]  # 포인터 초기화
                    cell[i][j] = 'EMPTY'  # 값 초기화
        cell[r][c] = value  # 원래 위치의 셀 값을 복원
        
    def pprint(r, c):
        c_r, c_c = check[r][c]  # 포인터에서 실제 위치(rr, cc) 가져옴
        answer.append(cell[c_r][c_c])  # 셀 값 결과 리스트에 추가
        
    # 메인 루프
    for i in commands:
        a = i.split(' ')  # 공백을 기준으로 커맨드와 인자들을 분리
        if a[0] == 'UPDATE':
            if len(a) == 4:
                insert(int(a[1]), int(a[2]), a[3]) 
            else:
                update(a[1], a[2]) 
        elif a[0] == 'MERGE':
            merge(int(a[1]), int(a[2]), int(a[3]), int(a[4]))  
        elif a[0] == 'UNMERGE':
            unmerge(int(a[1]), int(a[2]))  
        else:
            pprint(int(a[1]), int(a[2]))  
            
    return answer