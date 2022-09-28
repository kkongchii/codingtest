def solution():
    k = input()
    num = list(map(int, input().split()))     
    num1 = set(num)
    num1 = list(num1)
    num1.append(0)
    num1.sort(reverse=True)
    
    for i in range(len(num1)):
        if num1[i] == num.count(num1[i]):
            print(num1[i])
            return
        if num1[i] == 0:
            print(-1)
            return
    
    print(0)
    
solution()