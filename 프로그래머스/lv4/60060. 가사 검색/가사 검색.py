# 효율성이 있는거 보니 일일히 비교하는건 아닌가봄
# 해시로 words 애들을 다 key로 생성?

from collections import defaultdict
from bisect import bisect_left, bisect_right


def countsByRange(nums, left_value, right_value):
    r_i = bisect_right(nums, right_value)
    l_i = bisect_left(nums, left_value)
    return r_i-l_i

def solution(words, queries):
    answer = []
#     wordDict = defaultdict(int)
    
#     for word in words:
#         n = len(word)
#         for i in range(n):
#             wordDict[word[:i] + "?"*(n-i)] += 1
#             wordDict["?"*(n-i) + word[-i:]] += 1
    
#     for query in queries:
#         answer.append(wordDict[query])
        
    # 너무 쉽게 풀린다했어 -> 4,5 시간초과
    
    # 이진탐색 키워드가 질문하기에서 보인다 -> 정렬 필요, 저번에 진혁이가 말한 bisect 써볼 기회다
    # a??를 aaa~azz 사이 개수를 세도록 하면 해당 단어 셀 수 있음
    # r_words = []
    # for word in words:
    #     r_words.append(word[::-1])
    # words.sort()
    # r_words.sort()
    
    newDict = [[] for _ in range(10001)]
    r_newDict = [[] for _ in range(10001)]
    for word in words:
        newDict[len(word)].append(word)
        r_newDict[len(word)].append(word[::-1])
        
    for i in range(10001):
        newDict[i].sort()
        r_newDict[i].sort()
    
    for query in queries:
        lenQuery = len(query)
        
        head = query.replace("?", "a")
        tail = query.replace("?", "z")
        
        # print(head, query, tail)
        
        # answer.append(countsByRange(words, head, tail))
        # 이게 그냥 정렬하면 길이는 신경안쓰고 체크해버리네
        # fro?? 에서 frozz 가 frozen보다 뒤이므로 얘도 세버려서 답이 안나옴
        # 그렇다면 길이별로 나누자 -> 나온 결과 중 길이 검사?
        
        if query[0] == "?":
            query = query[::-1]
            answer.append(countsByRange(r_newDict[len(query)], head[::-1], tail[::-1]))
        else:
            answer.append(countsByRange(newDict[len(query)], head, tail))

        
        # 일단 됐는데 ?가 앞에 있으면 결과가 바뀌네 -> 접두어일경우 뒤집는 코드 추가
    
        # cnt = 0
        # for i in range(h,t):
        #     if len(words[i]) == lenQuery:
        #         # print(words[i])
        #         cnt += 1
        # answer.append(cnt)
        # 여기가 너무 무식한듯, 시간초과 나옴, 단어를 길이별로 나눠놓자
        
    return answer