def solution():
    N= int(input())
    
    def facto(n):
        if n<=1:
            return 1
        return n*facto(n-1)
    
    s = str(facto(N))
    cnt = 0
    flag = 1
    while(flag):
        if int(s)%10 != 0:
            flag = 0
        else:
            cnt += 1
            s = s[:-1]
            
    print(cnt)
          
solution()