
def solution():
    candidateNumber = int(input())
    candidate = []
    steal = 0
    
    for _ in range(candidateNumber):
        candidate.append(int(input()))
    
    if candidateNumber == 1:
        print(steal)
        return
    
    while(max(candidate[1:]) >= candidate[0]):
        election = candidate[1:].index(max(candidate[1:]))+1
        candidate[election] -= 1
        candidate[0] += 1
        steal += 1
        
    print(steal)
        
        
solution()

