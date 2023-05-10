def solution(brown, yellow):
    all_tiles = brown + yellow
    divisor = []
    for i in range(3, all_tiles//3+1):
        if all_tiles%i == 0:
            divisor.append(i)
    len_divisor = len(divisor)
    for i in range(len_divisor):
        height = divisor[i]
        for j in range(i, len_divisor):
            width = divisor[j]
            # print(divisor[j], divisor[i])
            if ((width+height)*2-4 == brown) and ((width-2)*(height-2) == yellow):
                answer = [width,height]
                return answer
    return -1