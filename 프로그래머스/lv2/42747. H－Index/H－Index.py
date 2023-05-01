def solution(citations):
    
    citations.sort(reverse=True)
    answer = len(citations)
    
    for h, paper in enumerate(citations):
        print(h+1, paper)
        if (h+1)>paper:
            answer = h
            break
    return answer