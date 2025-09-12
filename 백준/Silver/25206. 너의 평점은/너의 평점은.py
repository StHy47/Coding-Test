cr_sum = 0
answer = 0
for _ in range(20):
    subject, credit, score = input().split()
    credit = float(credit)
    if score == 'P':
        continue
    else: 
        cr_sum += credit
        if score == 'A+':
            n = 4.5
        elif score == 'A0':
            n = 4.0
        elif score == 'B+':
            n = 3.5
        elif score == 'B0':
            n = 3.0
        elif score == 'C+':
            n = 2.5
        elif score == 'C0':
            n = 2.0
        elif score == 'D+':
            n = 1.5
        elif score == 'D0':
            n = 1.0
        else:
            n = 0
        
        answer += (credit * n)
    
print(answer / cr_sum)
