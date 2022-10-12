def solution():
    N, M = map(int, input().split())
    if N == 0:
        print(0)
        return
    
    books = list(map(int, input().split()))
    box = 1
    weight = 0
    for book in books:
        if weight+book > M:
            box += 1
            weight = book
        else:
            weight += book
    
    print(box)
          
solution()