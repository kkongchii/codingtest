def solution():
    switchNums = int(input())
    switches = list(map(bool, map(int,input().split())))
    studentNum = int(input())
    
    def boyDo(current, switchNums, N):
        for i in range(N, switchNums+1, N):
            current[i-1] = not(current[i-1])
    
    def girlDo(current, switchNums, N):
        current[N] = not(current[N])
        for i in range(1,switchNums-N):
            if current[N-i]!=current[N+i] or N-i not in range(switchNums) or N+i not in range(switchNums):
                return
            else:
                current[N-i] = not(current[N-i])
                current[N+i] = not(current[N+i])
                
    def printBoolToInt(list):
        for i in range(len(list)):
            print(int(list[i] == True), end='')
            if i%10 == 9:
                print('')
            else:
                print(' ', end='')
            
               
    for _ in range(studentNum):
        gender, k = map(int,input().split())
        if gender == 1:
            boyDo(switches, switchNums, k)
        else:
            girlDo(switches, switchNums, k-1)
    
    printBoolToInt(switches)
     
solution()

