# # 되게 당연하게 이렇게 풀릴거 같은데 안풀린다
# # 재귀로 풀면 뭔가 이쁠거 같은데 생각이 안난다.
# def recursive(name, cur_cursor):
#     print("--------------------------")
#     name_copy = name.copy()
#     if sum(name) == 0:
#         print("end")
#         return 0

#     left, right = 1, 1
#     i = 1
#     while True:
#         # print(name[cur_cursor-i])
#         if name[cur_cursor-i] != 0:
#             name[cur_cursor-i] = 0
#             print("go left")
#             left += recursive(name, cur_cursor-i)
#             break
#         i += 1
        
#     i = 1
#     while True:
#         # print(name_copy[cur_cursor+i])
#         if name_copy[cur_cursor+i] != 0:
#             name_copy[cur_cursor+i] = 0
#             print("go right")
#             right += recursive(name_copy, cur_cursor+i)
#             break
#         i += 1
    
#     print(left, right, "min is ", min(left, right))
#     return min(left, right)
            
    

# def solution(name):
#     name = [min(ord(i)-65, 91 - ord(i)) for i in name]    
#     answer = sum(name) # 위 아래 총 이동횟수
#     cur_cursor = 0
#     name[0] = 0
#     # print(name)
    
#     answer += recursive(name, cur_cursor)

#     print("answer is ", answer)
#     return answer

def solution(name):

	# 조이스틱 조작 횟수 
    answer = 0
    
    # 기본 최소 좌우이동 횟수는 길이 - 1
    min_move = len(name) - 1
    
    for i, char in enumerate(name):
    	# 해당 알파벳 변경 최솟값 추가
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
            
        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
        min_move = min([min_move, 2 *i + len(name) - next, i + 2 * (len(name) -next)])
        
    # 알파벳 변경(상하이동) 횟수에 좌우이동 횟수 추가
    answer += min_move
    return answer