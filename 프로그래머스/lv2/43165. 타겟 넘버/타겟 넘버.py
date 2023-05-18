from collections import deque
def solution(numbers, target):
    answer = 0
    dq = deque()
    depth = 0
    dq.append((0,-1))
    n = len(numbers)
    while depth < n:
        number = numbers.pop()
        while dq[0][1] <= depth:
            node = dq.popleft()
            dq.append((node[0]+number, depth+1))
            dq.append((node[0]-number, depth+1))
        depth += 1
    
    for leaf in dq:
        if leaf[0] == target:
            answer += 1
            
    print(answer)
    return answer