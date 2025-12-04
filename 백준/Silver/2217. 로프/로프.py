n = int(input())
rope = []
for _ in range(n):
    r = int(input())
    rope.append(r)

rope = sorted(rope)

### 최소값
max_weight = 0
num = len(rope)

for i in range(num):
    weight = rope[i] * (num-i)
    max_weight = max(max_weight, weight)
    
        
print(max_weight)