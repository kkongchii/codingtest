
def solution():
    N, M = map(int, input().split())
    
    if N == 0 or M == 0:
        print(0)
        return
    
    package = 1000
    piece = 1000
    for _ in range(M):
        a, b = map(int, input().split())
        if a<package:
            package = a
        if b<piece:
            piece = b
    
    # print(package, piece)
    count = 0
    price = 0
    
    if piece<(package/6.0):
        price = piece*N
    else:
        while((N-count)>=6):
            price += package
            count += 6
            # print(price)
        if (price+package)>(price+piece*(N-count)):
            price = price+piece*(N-count)
        else:
            price += package
    
    print(price)
            
solution()