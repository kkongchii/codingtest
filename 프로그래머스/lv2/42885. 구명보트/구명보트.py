# 뭐하러 무인도에 50000명이나 가,,, 그게 무인도냐?
# 맨 앞사람부터 태우고 무게 제한까지 추가하면서 그리디하게 풀어보자

from collections import deque
def solution(people, limit):
    cnt = 0
    dq = deque(sorted(people))
    
    while len(dq) > 1:
        if dq[-1]+dq[0] <= limit:
            dq.popleft()
            dq.pop()
        else:
            dq.pop()
        cnt += 1
    
    if len(dq) == 1:
        cnt += 1

    print(cnt)
    answer = cnt
    return answer


# 이것도 아니네 가벼운 사람부터 내보내는게 아닌가보다
# 질문하기에서 찾아보니까 무거운사람과 가벼운 사람을 세트로 내보내는게 핵심인가보다
# 최대 2명인걸 못봤네... 문제를 잘 읽자
# def solution(people, limit):
#     cnt = 0
#     index = 0
#     people.sort()
#     while index < len(people):
#         boat = 0
#         while True:
#             if index >= len(people):
#                 break
#             if (boat+people[index]) <= limit:
#                 boat += people[index]
#                 # print(index, "번째 승객 탈출, 무게 = ", people[index])
#                 index += 1
#             else:
#                 break
#         cnt += 1

#     answer = cnt
#     return answer


# 이렇게 하면 시간초과 걸릴듯, 정렬하고 하자
# def solution(people, limit):
#     cnt = 0
#     while sum(people) != 0:
#         boat = 0
#         for i in range(len(people)):
#             if people[i] != 0 and (boat+people[i]) <= limit:
#                 boat += people[i]
#                 people[i] = 0
#         cnt += 1
#         # print(people, boat, cnt)
    
#     # print(cnt)
#     answer = cnt
#     return answer