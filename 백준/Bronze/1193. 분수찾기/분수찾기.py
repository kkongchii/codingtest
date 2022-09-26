def solution():
    x = int(input())
    index = -1
    for i in range(1,4500):
        n = i*(i+1)/2
        if x <= n:
            index = i
            break;
        
    k = x-(index*(index-1)/2)
    if index%2 == 0:
        print('%d/%d' % (int(k), int(index-k+1)))
    else:
        print('%d/%d' % (int(index-k+1), int(k)))
    
solution()