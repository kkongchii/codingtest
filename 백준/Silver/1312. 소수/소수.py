def solution():
    A, B, N = map(int, input().split())
    
    for i in range(N+1):
        tmp = A/B
        k = int(tmp)
        A = (A%B)*10
        
    print(k)
                    
solution()

# 단순 나눗셈 하고 문자열 변환 하는 방법으로 구현 불가능
# Python은 15자리까지 구현, N은 백만까지 지정 가능
# 수학적 원리 사용해서 구현해야 함