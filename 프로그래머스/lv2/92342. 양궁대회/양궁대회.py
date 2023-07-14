# 중복조합 완전탐색
from itertools import combinations_with_replacement
from collections import Counter, defaultdict
def solution(n, info):
    answer = {}
    info.reverse()
    cases = list(combinations_with_replacement([0,1,2,3,4,5,6,7,8,9,10], n))
    apeach = dict()
    for i in range(11):
        apeach[i] = info[i]
    maxDiff = 0
    bestCase = -1
    for case in cases:
        lion = Counter(case)
        l_score = 0
        a_score = 0
        for i in range(11):
            if lion[i] == 0 and apeach[i] == 0:
                continue
            if lion[i]>apeach[i]:
                l_score += i
            else:
                a_score += i
        diff = l_score-a_score
        if l_score>a_score and diff>maxDiff:
            # print(lion, l_score)
            bestCase = lion
            maxDiff = diff
    for i in range(11):
        answer[i] = 0
    
    if bestCase != -1:
        for i in bestCase.keys():
            answer[i] = bestCase[i]
        answer = list(answer.values())
        answer.reverse()
    else:
        answer = [-1]
        
    return answer