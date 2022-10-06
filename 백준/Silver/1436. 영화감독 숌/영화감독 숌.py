def solution():
    N = int(input())
    tmp = 666
    k = 0
    
    while(k != N):
        if '666' in str(tmp):
            k += 1
        tmp += 1
    
    print(tmp-1)

solution()