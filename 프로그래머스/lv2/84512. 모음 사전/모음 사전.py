# 5, 25, 125, 625, 3125 = 3905

from itertools import product

def solution(word):
    dic = []
    vowel = ['A', 'E', 'I', 'O', 'U']
    for i in range(1, 6):
        tmp = product(vowel, repeat = i)
        for w in tmp:
            dic.append(''.join(w))
    dic.sort()
    answer = dic.index(word)+1
    return answer