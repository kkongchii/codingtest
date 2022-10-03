def solution():
    X = int(input())
    
    list64 = [64, 32, 16, 8, 4, 2, 1]
    binaryX = []
    while(X>1):
        binaryX.append(X%2)
        X = int(X/2)
    
    binaryX.append(1)
    binaryX.reverse()
    print(binaryX.count(1))
solution()
#X를 이진수로 바꿔서 1의 개수 세면 됨