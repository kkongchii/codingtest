
def solution():
    N = list(input())
    l = [0]*9
    cnt = 0
    
    for i in range(len(N)):
        number = int(N[i])
        if number == 9:
            number = 6
        if l[number] == 0:
            cnt += 1
            l = [l[j]+1 for j in range(len(l))]
            l[6] += 1
        l[number] -= 1
        
    print(cnt)
          
solution()