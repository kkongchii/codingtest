# depth에 따라 ~2^1, ~2^3, ~2^7 순으로 표현 가능
# 1,3->2 / 5,7->6, 1,2,3,5,6,7->4
# 1111111 / 111111111111111
# 반절 나눠서 중간 위치가 1이여야 양쪽 존재 가능
# 또 그 반절 중 중간 위치가 1이여야 양쪽 존재 가능
# 반복해서 검사?
def rec(num):
    mid = len(num)//2
    # print(num, num[mid])
    if mid == 0:
        return True
    # 조건 추가
    if '1' not in num or '0' not in num:
        return True
    if num[mid] == '0':
        return False
    return rec(num[:mid]) and rec(num[mid+1:])

def solution(numbers):
    answer = []
    binary = []
    for number in numbers:
        binary.append(str(bin(number))[2:])
    binarys = [ bin(x)[2:] for x in numbers]
    b_list = [ 2**x - 1 for x in range(50)]
    for binary in binarys:
        l = len(binary)
        for b in b_list:
            if l <= b:
                binary = (b-l)*'0'+binary
                break
        # print(binary)
        # 2^n-1 개수만큼 0으로 패딩
        # 이제 절반씩 나눠서 가운데수가 1인지 검사 => 중간인덱스가 0이면 stop -> 재귀?
        if rec(binary):
            answer.append(1)
        else:
            answer.append(0)
        
    return answer