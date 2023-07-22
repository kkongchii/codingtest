# 쿼리 10만, 지원자 5만 -> 각 쿼리에 대해 모든 지원자 검사시 50억 너무 많긴 함, 효율성 검사도 한댔으니
# 해시로? 각 분야 별 h[java] = {1,45,88,100, ...} 싹 구해서 교집합 처리
# def dupKey(keyList):
#     if keyList.count("")
#     # 재귀 함수 짜지 말고 다르게 가보자

from collections import defaultdict
from itertools import combinations
def solution(info, query):
    answer = []
    infoDict = defaultdict(list)
    for i in range(len(info)):
        s = info[i].split(" ")
        score = int(s.pop())
        for j in range(5):
            for c in combinations(s, j):
                key = ''.join(c)
                infoDict[key].append(score)

    for value in infoDict.values():
        value.sort()
    # print(infoDict)
    
    for q in query:
        s = q.split(" and ")
        score = s[-1].split(" ")
        s[-1] = score[0]
        score = int(score[1])
        
        while "-" in s:
            s.remove("-")
        s = ''.join(s)
        
        if s in infoDict:
            head, tail = 0, len(infoDict[s])
            while head != tail and head != len(infoDict[s]):
                if infoDict[s][(head + tail) // 2] >= score:
                    tail = (head + tail) // 2
                else:
                    head = (head + tail) // 2 + 1
            answer.append(len(infoDict[s]) - head)
        else:
            answer.append(0)
        # cnt = 0
        # if s in infoDict:
        #     for applicant in infoDict[s]:
        #         if applicant >= score:
        #             cnt += 1
        #         else:
        #             break
        # answer.append(cnt)
        # 질문하기 보니까 이분탐색 쓰라고하네
            # - 포함은 그냥 카운트할 때 처리해야 할듯, 해당하는 키를 판별하기가 쉽지 않음
        # answer.append(len(list(filter(lambda x: x > score, s))))
#     for q in query:
#         s = q.split(" and ")
#         score = s[-1].split(" ")
#         s[-1] = score[0]
#         score = score[1]
        
#         tmp = set(list(range(len(info))))
#         for i in range(len(s)):
#             if s[i] == "-":
#                 continue
#             tmp = tmp & set(infoDict[s[i]])
#         count = 0
#         # for appli in list(tmp):
#         #     if int(info[appli].split(" ")[-1]) >= int(score):
#         #         count += 1
#         answer.append(count)
# 점수 찾는 파트 문제가 아님, 교집합 알고리즘만 두고 돌려도 시간초과 뜸
# 새로운방법 -> 각 카테고리 별 항목이 두세개 뿐인데 모든 조합?
            
    return answer
