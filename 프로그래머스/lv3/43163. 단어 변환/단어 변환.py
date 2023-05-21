from collections import deque

# def BFS(begin, target, visited): 막상 구현해놓으니까 그냥 solution에 옮기는게 나을듯
    

def solution(begin, target, words):
    answer = 0
    words = [begin]+words
    visited = [False]*len(words)
    dq = deque()
    dq.append((0, begin))
    while dq:
        node = dq.popleft()
        depth = node[0]
        visited[words.index(node[1])] = True
        if node[1] == target:
            answer = depth
            break
        for i in range(len(words)):
            tmp = 0
            if visited[i] == False:
                for j in range(len(words[i])):
                    if node[1][j] != words[i][j]:
                        tmp += 1
                if tmp == 1:
                    visited[i] = True
                    dq.append((depth+1,words[i]))
    return answer