import itertools
def solution(users, emoticons):
    ## 가능한 할인율 경우의 수 
    per_list = [10,20,30,40]
    sale_per = itertools.product(per_list, repeat=len(emoticons))
    sale_per = [list(i) for i in sale_per]
    
    best_plus = 0 ## 최대 구매자
    best_price = 0 ## 최고가

    ### 가능한 할인율 경우의 수에 따른 유저의 구매
    for i in range(len(sale_per)):
        e_plus = 0 #임티플 구매자 변수 생성 및 초기화
        total_price = 0 #총 구매값 변수 생성 및 초기화
        buy = [[k, 0] for k in range(len(users))]  # 구매 기록 생성 및 초기화
        for j in range(len(emoticons)):
            ej_price = emoticons[j] * (100 - sale_per[i][j])/100 ##j번째 이모티콘 가격
            for k in range(len(users)):
            ## j번째 이모티콘 할인율이 user의 기준보다 크면 구매
                if users[k][0] <= sale_per[i][j]:
                    buy[k][1] += ej_price
        ## 구매자별 총 가격이 사용자 가격 이상이면 사용자는 임티플 구매
        for k in range(len(buy)):
            if buy[k][1] >= users[k][1]:
                buy[k][1] = 0
                e_plus += 1
            total_price += buy[k][1]
                
        ### 현재 임티플 구매자와 비교해서 최대값이면 해당 할인율로 갱신
        ### 만약에 임티플 구매자 수가 같다면 금액 비교해서 더 큰값으로 할인율 갱신
        if e_plus > best_plus or (e_plus == best_plus and best_price < total_price):

            best_plus = e_plus
            best_price = total_price
            
    
    answer = [best_plus, best_price]
    return answer