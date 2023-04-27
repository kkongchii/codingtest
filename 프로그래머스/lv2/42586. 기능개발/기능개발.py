def solution(progresses, speeds):
    answer = []
    while progresses:
        i = 0
        print(progresses)
        progresses = [x+y for x,y in zip(progresses, speeds)]
        while progresses and progresses[0] >= 100:
            i = i+1
            progresses.pop(0)
            speeds.pop(0)
        if i>0:
            answer.append(i)
    return answer