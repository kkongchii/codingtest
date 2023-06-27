# from collections import defaultdict
def solution(N, number):
    # case = defaultdict(list)
    case = [[], [N]]
    if N == number:
        return 1
    for i in range(2,9): # 8보다 크면 -1
        case.append([int(str(N)*i)])
        for j in range(1, i//2+1):
            for k in case[j]:
                for d in case[i-j]:
                    case[i].append(k+d)
                    case[i].append(k-d)
                    case[i].append(d-k)
                    case[i].append(d*k)
                    if d:
                        case[i].append(k/d)
                    if k:
                        case[i].append(d/k)
        if number in case[i]:
            return i
    return -1