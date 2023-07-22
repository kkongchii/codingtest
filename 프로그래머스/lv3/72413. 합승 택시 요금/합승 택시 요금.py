# 대놓고 다익스트라 냄새가 난다
# 하지만 합승 조건이 있으므로 경유지를 감안해서 계산하자
# 경유지까지 비용 + 경유지부터 A도착지 + 경유지부터 B도착지
# 첫 지점도 경유지라고 생각하면 출발부터 따로 가는 경우까지 생각 가능
# 그러면 각 노드에서 다른 모든 노드로 가는 비용을 전부 계산? 노드 갯수 200개 200*199 대충 4만개 할만한듯
# 다익스트라 1.시작노드에서 갈수있는 경로 비용 초기화 2.가장 비용이 싼 노드로 넘어가서 탐색 3.거쳐가는 비용vs기존비용
import heapq
from math import inf

def dijkstra(n, table, start):
    
    hq = []
    fee = [inf for _ in range(n)]
    fee[start] = 0
    heapq.heappush(hq, [fee[start], start]) # heapq 정렬 때문에 비용을 앞으로
    
    while hq:
        node = heapq.heappop(hq)
        if fee[node[1]] < node[0]:
            continue
        for i in range(n):
            newFee = fee[node[1]] + table[node[1]][i]
            if newFee < fee[i]:
                fee[i] = newFee
                heapq.heappush(hq, [fee[i], i])
    # print(fee)
    return fee
        
    

def solution(n, s, a, b, fares):
    answer = inf
    hq = []
    graph = [[inf] * n for _ in range(n)]
    for fare in fares:
        i, j ,fee = fare
        graph[i-1][j-1] = fee
        graph[j-1][i-1] = fee
    # print(graph)
    feeTable = []
    for i in range(n):
        feeTable.append(dijkstra(n, graph, i))
    # print(feeTable)
    
    for i in range(n):
        answer = min(answer, feeTable[s-1][i]+feeTable[i][a-1]+feeTable[i][b-1])
    
    
    return answer