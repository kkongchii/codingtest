# 문제에서 그리디 냄새가 나는데 완전탐색인가?
# 던전 수가 8개이므로 8!이여서 할만할듯 그래서 완전탐색인가
from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for cases in permutations(dungeons, len(dungeons)):
        health = k
        count = 0
        for dungeon in cases:
            if health >= dungeon[0]:
                health -= dungeon[1]
                count += 1
        if count > answer:
            answer = count
    return answer