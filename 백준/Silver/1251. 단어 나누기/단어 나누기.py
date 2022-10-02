
def solution():
    word = list(input())
    wordList = []

    for i in range(len(word)-2):
        for j in range(i+1, len(word)-1):
            a = word[:i+1]
            b = word[i+1:j+1]
            c = word[j+1:]
            a.reverse()
            b.reverse()
            c.reverse()
            tmp = ''.join(a) + ''.join(b) + ''.join(c)
            wordList.append(tmp)
    wordList.sort()
    print(wordList[0])
        
solution()

# 브루트포스는 진짜 다 구해서 정렬하고 맨 앞 원소 출력하는 방식
# 굳이 어렵게 가지 말자