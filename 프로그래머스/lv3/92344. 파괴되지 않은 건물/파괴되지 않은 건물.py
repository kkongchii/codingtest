# 느낌이 3중 for문 당연히 안될것 같긴한데
# def solution(board, skills):
#     answer = 0
#     for skill in skills:
#         for i in range(skill[1], skill[3]+1):
#             for j in range(skill[2], skill[4]+1):
#                 if skill[0] == 1:
#                     board[i][j] -= skill[5]
#                 elif skill[0] == 2:
#                     board[i][j] += skill[5]
#     for row in board:
#         for el in row:
#             if el > 0:
#                 answer += 1
    # 효율성에서 당연히 다 떨어짐 ㅋㅋ
    
    # 모르겠어서 질문하기에 있는 정보 참고해서 부분합에 대해 공부해옴
    
    
    
    # return answer
    
def solution(board, skill):
    answer = 0
    n = len(board) #행
    m = len(board[0]) #열
    board_sum = [[0]*(m+1) for _ in range(n+1)] #누적합 저장하는 배열
    
            
    for ty_pe, r1, c1, r2, c2, degree in skill:
        if ty_pe == 1:
            board_sum[r1][c1] -= degree
            board_sum[r1][c2+1] += degree
            board_sum[r2+1][c1] += degree
            board_sum[r2+1][c2+1] -= degree
        else:
            board_sum[r1][c1] += degree
            board_sum[r1][c2+1] -= degree
            board_sum[r2+1][c1] -= degree
            board_sum[r2+1][c2+1] += degree
                    
    for i in range(n):
        for j in range(1, m):
            #누적합 구하기. 왼쪽에서 오른쪽으로
            board_sum[i][j] += board_sum[i][j-1] #O(n*m)
            
    for i in range(1, n):
        for j in range(m):
            #누적합 구하기. 위에서 아래로
            board_sum[i][j] += board_sum[i-1][j] #O(n*m)
    
    for i in range(n):
        for j in range(m):
            board[i][j] += board_sum[i][j] #O(n*m)
            if board[i][j] > 0:
                answer += 1
        
                    
        
    return answer