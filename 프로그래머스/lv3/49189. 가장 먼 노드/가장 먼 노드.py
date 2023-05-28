# BFS? 모든 노드 다 탐색하고 길이 가장 긴 애들 출력
# 근데 이거 20000에 50000인데 가능?
from collections import deque

def solution(n, edge):
    answer = 0
    dq = deque()
    visit = [0]*(n+1)
    edgeList = [[] for _ in range(n+1)]
    for s, d in edge:
        edgeList[s].append(d)
        edgeList[d].append(s)
        # 양방향 간선
    visit[1] = 1
    dq.append(1)
    while dq:
        node = dq.popleft()
        for k in edgeList[node]:
            if visit[k] == 0:
                visit[k] = visit[node]+1
                dq.append(k)
    
    answer = visit.count(max(visit))
    return answer