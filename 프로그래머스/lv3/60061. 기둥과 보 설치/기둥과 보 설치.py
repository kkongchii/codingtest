# 재밌겠다
# 각 동작에 대해 유효성 검증 후 -> 계속 board에 업데이트
# [x좌표, y좌표, 0(기둥)/1(보), 0(삭제)/1(설치)]
# 기둥은 교차점 기준 위로, 보는 교차점 기준 오른쪽으로

# def check(board, op):
#     if op[3]: # 설치
#         if op[2] == 0: # 기둥
#             if op[0] == 0: # 바닥에 설치
#                 return True
#             if board[op[1]][op[0]] == 1: # 기준점에 뭔가 있는 경우
#                 return True
#             return False
#         if op[2] == 1: # 보
#             # 한쪽 끝이 기둥 위에 있는 경우 -> 양 끝이 1이고 그 아래도 1
#             # 양쪽 끝이 보와 연결될 경우 -> 양끝이 1이고 각각의 왼쪽/오른쪽도 1
#             if board[op[1]][op[0]] == 1 and board[op[1]-1][op[0]] == 1:
#                 return True
#             elif board[op[1]][op[0]+1] == 1 and board[op[1]-1][op[0]+1] == 1:
#                 return True
#             elif board[op[1]][op[0]] == 1 and board[op[1]][op[0]+1] == 1 and board[op[1]][op[0]+2] == 1 and board[op[1]][op[0]-1] == 1:
#                 return True
#     else: # 삭제
#         return True
    
#     return False

# def solution(n, build_frame):
#     answer = [[]]
#     board = [[0]*(n+1) for _ in range(n+1)]
#     print(board)
#     # 아 문제 끝까지 읽고 함수 작성할걸
    
    
#     for op in build_frame:
#         if check(board, op): # 유효성 검증
#             if op[3]: # 설치
#                 if op[2] == 0: # 기둥
#                     board[op[1]][op[0]] = 1
#                     board[op[1]+1][op[0]] = 1
#                 if op[2] == 1: # 보
#                     board[op[1]][op[0]] = 1
#                     board[op[1]][op[0]+1] = 1
#             else: # 삭제
#                 if op[2] == 0: # 기둥
#                     board[op[1]][op[0]] = 0
#                     board[op[1]+1][op[0]] = 0
#                 if op[2] == 1: # 보
#                     board[op[1]][op[0]] = 0
#                     board[op[1]][op[0]+1] = 0
#     print(board)



def check(answer):
    flag = True
    for x,y,a in answer:
        if a == 0: # 기둥
            # 땅에 박혀있거나(교차점 y좌표가 0) / 보 위에 있거나(교차점이 보의 교차점 위거나, 그 옆칸의 위거나)
            # 기둥 위에 있거나(교차점이 기둥의 교차점 한칸 위거나)
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                flag = True
            else:
                flag = False
                break
        if a == 1:
            # 한쪽 끝이 기둥 위에 있는 경우 -> 교차점과 그 오른쪽 좌표가 기존 기둥좌표 한칸 위와 겹치는지
            # 양쪽 끝이 보와 연결될 경우 -> 교차점이 기존 보 왼쪽 좌표와 겹치면서 교차점의 오른쪽 좌표가 기존 보 좌표와 겹치면
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                flag = True
            else:
                flag = False
                break
    return flag

def solution(n, build_frame):
    answer = []
    # 아 문제 끝까지 읽고 함수 작성할걸, board가 아닌 교차점과 건축물 종류로 저장해야 할듯\
    # 그러면 각 op 넣고 유효성 체크하고 맞으면 남기고를 반복
    
    
    for op in build_frame:
        if op[3]:
            answer.append([op[0], op[1], op[2]])
            if not check(answer):
                answer.remove([op[0], op[1], op[2]])
        else:
            answer.remove([op[0], op[1], op[2]])
            if not check(answer):
                answer.append([op[0], op[1], op[2]])
    
    # sort가 요구조건에 있는거 놓치지말기
    answer.sort()
    # print(answer)
    return answer