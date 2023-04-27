def solution(priorities, location):
    operate = 0
    while priorities:
        print(priorities, location)
        if priorities.index(max(priorities)):
            priorities.append(priorities.pop(0))
            if location <= 0:
                location = len(priorities)-1
            else:
                location -= 1
        else:
            priorities.pop(0)
            operate += 1
            if location == 0:
                break
            else:
                location -= 1
        
    answer = operate
    return answer