
def solution():
    N = int(input())
    count = 99
    for i in range(100,N+1):
        isCorrect = 1
        temp = str(i)
        diff = int(temp[1])-int(temp[0])
        for j in range(len(temp)-1):
            if (int(temp[j])+diff) != int(temp[j+1]):
                isCorrect = 0
                break
        if isCorrect:
            count += 1
    if N<100:
        print(N)
    else:
        print(count)
    
            
solution()