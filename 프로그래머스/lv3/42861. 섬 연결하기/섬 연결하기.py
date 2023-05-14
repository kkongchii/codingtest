# 최단거리 알고리즘,,, 뭐더라,,, 크루스칼,,,
# https://velog.io/@kimdukbae/%ED%81%AC%EB%A3%A8%EC%8A%A4%EC%B9%BC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Kruskal-Algorithm
# 1.간선의 비용 기준으로 정렬
# 2.첫 간선부터 추가하여 싸이클이 없는지 확인하여 없다면 추가
# 2-1. 어떻게 확인? 새 간선의 양쪽 노드가 이미 메인 트리에서 연결되어 있는지 검사
def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2])
    tree = [costs[0][0], costs[0][1]]
    answer += costs[0][2]
    
    while len(tree) < n:
        for cost in costs:
            if cost[0] in tree and cost[1] in tree:
                continue
            elif cost[0] in tree:
                tree.append(cost[1])
                answer += cost[2]
                break
            elif cost[1] in tree:
                tree.append(cost[0])
                answer += cost[2]
                break
                
    print(answer)

    
    return answer