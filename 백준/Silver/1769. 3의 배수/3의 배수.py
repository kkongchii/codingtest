def solution():
    N = input()
    
    def recursion(N, count):
        if len(N)>1:
            count+=1
            t=0
            for i in N:
                t += int(i)
            recursion(str(t), count)
        else:
            if (int(N)%3) == 0:
                print(count)
                print("YES")
            else:
                print(count)
                print("NO")
    count = 0
    recursion(N, count)
 
solution()