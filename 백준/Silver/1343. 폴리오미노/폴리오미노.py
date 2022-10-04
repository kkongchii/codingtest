def solution():
    board = input()
    XList = board.split('.')
    answer = []
    
    for i in range(len(XList)):
        XLength = len(XList[i])
        tmp = 0
        tmpA = 0
        tmpB = 0
        if XLength == 0:
            answer.append('')
            continue
        while(tmp<=XLength):
            tmp += 4
            tmpA += 1
        tmp -= 4
        tmpA -= 1
        while(tmp<=XLength):
            tmp += 2
            tmpB += 1
        tmp -= 2
        tmpB -= 1
        if tmp == XLength:
            poly = 'A'*4*tmpA
            poly = poly + 'B'*2*tmpB
            answer.append(poly)
        else:
            print(-1)
            return
        
    print('.'.join(answer))
    
solution()