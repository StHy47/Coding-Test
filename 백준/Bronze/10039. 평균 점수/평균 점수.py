score = 0
for _ in range(5):
    s = int(input())
    if s < 40 :
        s = 40
    else:
        s = s
    score = score + s
    
print(score//5)