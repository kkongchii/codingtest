from collections import deque


def solution(info, edges):
    n = len(info)
    tree = [[] for _ in range(n)]
    answer = 1  # 루트 노드는 양

    for edge in edges:
        tree[edge[0]].append(edge[1])

    # BFS
    dq = deque([[tree[0], 1, 1]])  # 연결 노드, 양의 수 + 늑대 수, 총 양의 수

    while dq:
        node = dq.popleft()

        for i, next_node in enumerate(node[0]):

            total = node[2]
            if info[next_node] == 0:  # 양
                cal = node[1] + 1
                total += 1

            else:
                cal = node[1] - 1  # 늑대

            if cal > 0:  # 양의 수 > 늑대 수
                dq.append([node[0][:i] + node[0][i+1:] + tree[next_node], cal, total])
                answer = max(answer, total)

    return answer