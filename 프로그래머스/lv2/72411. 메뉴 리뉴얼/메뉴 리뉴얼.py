from collections import Counter
from itertools import combinations
# 많이 주문된 단품 메뉴를 카운트해서 체크? -> 그리디
# 그냥 조합? 알파벳 26갠데 가능하려나 -> 완전탐색
# course당 하나씩;; 문제가 좀 설명이 모자란데
def solution(orders, course):
    answer = []
    combine = []
    # for order in orders:
    #     for i in course:
    #         combine += combinations(sorted(order), i)
    
    for i in course:
        combine = []
        for order in orders:
            combine += combinations(sorted(order), i)
        print(Counter(combine))
        cnt = Counter(combine)
        if cnt and max(cnt.values()) > 1:
            for c in cnt.items():
                if c[1] == max(cnt.values()):
                    answer.append(''.join(c[0]))
    answer.sort()
    print(answer)
        
    
    return answer