def solution():
    k = int(input())
    list = [0]
    for i in range(127):
        list.append(list[i]*10+4)
        list.append(list[i]*10+7)
    list.reverse()
    for i in range(len(list)):
        if list[i] <= k:
            print(list[i])
            return
                
solution()