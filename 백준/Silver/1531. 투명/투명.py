def solution():
    N, M = map(int, input().split())
    board = [[0]*100 for _ in range(100)]

    for _ in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        for i in range(x1-1, x2):
            for j in range(y1-1, y2):
                if board[i][j] <= M:
                    board[i][j] += 1
    
    answer = 0
    for k in range(100):
        answer += board[k].count(M+1)
    
    print(answer)
          
solution()