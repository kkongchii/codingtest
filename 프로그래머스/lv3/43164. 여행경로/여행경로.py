# 문제 없는 듯 했으나 sort해서 알파벳 앞선데를 가면 전체를 못 가는 경우가 생김
from collections import deque

# def solution(tickets):
#     tickets.sort(key=lambda x:x[1])
#     tickets = [(i, ticket) for i, ticket in enumerate(tickets)]
#     dq = deque()
#     first = 0
#     for ticket in tickets:
#         if ticket[1][0] == "ICN":
#             first = ticket
#             break
#     dq.append(first)
#     visited = [0]*len(tickets)
#     answer = ["ICN"]
#     print(tickets)
#     while dq:
#         print(dq)
#         node = dq.popleft()
        
#         if sum(visited) == len(visited):
#             answer.append(node[1][1])
#         tmp = []
#         for i in range(len(tickets)):
#             if node[1][1] == tickets[i][1][0] and visited[tickets[i][0]]==0:
#                 tmp.append(tickets[i])
#         print(tmp)
#         if len(tmp) != 0 or (len(tmp) == 0 and sum(visited) == len(visited) - 1):
#             dq.clear()
#             dq.extend(tmp)
#             answer.append(node[1][1])
#             visited[node[0]] = 1
        
#         print(visited)
#         print(answer)
            

#     return answer

# 아예 새로 풀자, 위처럼 접근하면 근본적인 문제가 해결이 안될 듯
def solution(tickets):
    answer = []
    dq = deque()
    dq.append(("ICN", ["ICN"], []))
    # 현재 위치, 경로, 사용한 티켓
    
    while dq:
        now, path, usedTickets = dq.popleft()
        if len(usedTickets) == len(tickets):
            answer.append(path)
            continue
        # 정답 후보 리스트에 추가
        # 현재 dq에서 꺼낸 튜플이 정답이리라는 보장은 없음
        # 모든 경우의 수를 탐색 중이며, 매 티켓마다 path가 서로 다름(현재 진행상황)
        # 어쨌든 티켓 다 쓴 케이스는 
        for i, ticket in enumerate(tickets):
            if ticket[0] == now and i not in usedTickets:
                dq.append((ticket[1], path+[ticket[1]], usedTickets+[i]))
                # 티켓을 하나씩 꺼내서 정답 경로에 추가가 아닌, 모든 경우의 수를 탐색
                
    answer.sort()
    # 그 중 알파벳이 앞선 
    return answer[0]
    