
def solution():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    sum = 0
    for _ in range(N):
        A_min = min(A)
        indexA = A.index(A_min)
        A[indexA] = 100
        
        B_max = max(B)
        indexB = B.index(B_max)
        B[indexB] = -1
        
        sum += A_min*B_max
        
    print(sum)
     
solution()