from collections import deque
def BFS(computers, i, visited):
    dq = deque()
    dq.append(i)
    while dq:
        node = dq.popleft()
        visited[node] = True
        for j, connect in enumerate(computers[node]):
            if connect and node!=j and visited[j]==False:
                dq.append(j)

def solution(n, computers):
    answer = 0
    visited = [False]*n
    
    for i in range(n):
        if visited[i]:
            continue
        BFS(computers, i, visited)
        answer += 1
    return answer