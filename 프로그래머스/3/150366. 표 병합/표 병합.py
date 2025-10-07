def solution(commands):
    answer = []
    # 빈 셀 50*50 생성
    cell = [['EMPTY' for _ in range(51)] for _ in range(51)]  
    # 셀 위치 확인용
    check = [[[i, j] for j in range(51)] for i in range(51)]
        
    # 메인 루프
    for i in commands:
        a = i.split(' ')  # 입력 하나씩 분리
        
        #1. 값 입력하기
        if a[0] == 'UPDATE':
            if len(a) == 4:
                r = int(a[1])
                c = int(a[2])
                c_r, c_c = check[r][c]
                cell[c_r][c_c] = a[3]
        
        # 2. 값1을 값2로 변경
            else:
                for i in range(51):
                    for j in range(51):
                        # 만약 값이 값1이면 해당 셀(i,j) 값을 값2로 변경
                        if cell[i][j] == a[1]:
                            cell[i][j] = a[2]
        
        # 3. 병합하기
        elif a[0] == 'MERGE':
            r1, c1 = int(a[1]), int(a[2])
            r2, c2 = int(a[3]), int(a[4])
            c_r1, c_c1 = check[r1][c1] # 셀1 위치 확인
            c_r2, c_c2 = check[r2][c2] # 셀2 위치 확인
            # 셀 값 가져오기
            v1, v2 = cell[c_r1][c_c1], cell[c_r2][c_c2]
            # 값 변경하기
            cell[c_r1][c_c1] = v2 if v1 == 'EMPTY' else v1
            for i in range(51):
                for j in range(51):
                    # 셀2의 위치를 셀1 위치로 변경
                    if check[i][j] == [c_r2, c_c2]:
                        check[i][j] = [c_r1, c_c1]
                        
        # 4. 병합 해제
        elif a[0] == 'UNMERGE':
            r, c = int(a[1]), int(a[2])
            # 위치 확인
            c_r, c_c = check[r][c]
            v = cell[c_r][c_c]  # 셀 값 가져오기
            for i in range(51):
                for j in range(51):
                    if check[i][j] == [c_r, c_c]:
                        check[i][j] = [i, j]
                        cell[i][j] = 'EMPTY'
            cell[r][c] = v
            
        # 5. print하기
        else:
            r, c = int(a[1]), int(a[2])
            # r,c 위치 확인
            c_r, c_c = check[r][c]
            answer.append(cell[c_r][c_c])
            
    return answer
