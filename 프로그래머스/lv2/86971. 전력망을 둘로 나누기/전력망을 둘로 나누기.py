# n이 최대 100이니까 다 잘라보고 찾아보자
from collections import deque

def bfs(v, n, grid):
    cnt = 0
    
    queue = deque()
    queue.append(v)
    
    visited = [0 for _ in range(n+1)]
    visited[v] = 1
    
    while queue:
        v = queue.popleft()
        
        for w in grid[v]:
            if not visited[w]:
                visited[w] = 1
                queue.append(w)
                cnt += 1
    
    return cnt

def solution(n, wires):
    answer = 100000
    graph = [[] for _ in range(n+1)] # 0번부터 노드가 시작되는 것이 아니기 때문에 +1

    for s, e in wires: # 양방향이기 때문에 양쪽 모두 추가
        graph[s].append(e)
        graph[e].append(s)
        
    print(graph)
    
    # 하나씩 연결을 끊고 개수 확인
    for i in range(n-1):
        graph[wires[i][0]].remove(wires[i][1])
        graph[wires[i][1]].remove(wires[i][0])
            
        cnt_node1 = bfs(wires[i][0], n, graph)
        cnt_node2 = bfs(wires[i][1], n, graph)
        
        answer = min(answer, abs(cnt_node1 - cnt_node2))
        
        graph[wires[i][0]].append(wires[i][1])
        graph[wires[i][1]].append(wires[i][0])
    
    return answer