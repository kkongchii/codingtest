import math # sqrt
def isPrime(n):
    for i in range(2,math.floor(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    subList = []
    transform = ''
    while n:
        transform = str(n%k) + transform
        n = n//k
    while True:
        if transform == '0':
            break
        if '0' not in transform:
            subList.append(transform)
            break
        index = transform.index('0')
        if transform[:index] != '':
            subList.append(transform[:index])
        
        transform = transform[index+1:]
        
    for num in subList:
        if isPrime(int(num)) and int(num) > 1:
            print(num)
            answer += 1
    
    # print(subList)
        
    
    return answer