chess = list(input().split())
chess = [int(x) for x in chess]
original = [1,1,2,2,2,8]

answer = []
for i in range(len(chess)):
    p_c = original[i] - chess[i]
    answer.append(p_c)
        
print(*answer)