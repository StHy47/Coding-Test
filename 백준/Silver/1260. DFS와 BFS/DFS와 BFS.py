n, m, v = map(int, input().split())

# 그래프 정보 저장
graph = {i: [] for i in range(1, n + 1)}

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for node in graph:
    graph[node].sort()
    
## dfs
def dfs(node, dfs_v):
    dfs_v.append(node)
    ## 순회
    ### 순서대로 방문
    for nb in graph[node]:
        if nb not in dfs_v:
            dfs(nb, dfs_v)
    return dfs_v
            
from collections import deque
## bfs
def bfs(node):
    visited = {node}
    queue = deque([node])
    
    bfs_v = []
    
    while queue:
        node = queue.popleft() 
        bfs_v.append(node)
        
        for neighbor in graph[node]: 
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return bfs_v

dfs_result= dfs(v,[])
bfs_result = bfs(v)

print(*dfs_result)
print(*bfs_result)