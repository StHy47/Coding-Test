h, w, n, m = map(int, input().split())
### 나올 수 있는 네모의 크기
s= h // (n+1)
g= w // (m+1)
## 만약 나머지가 있다면 거기도 사람 앉을 수 있음
if h % (n+1) != 0:
    s += 1
if w % (m+1) != 0:
    g += 1
print(s*g)
