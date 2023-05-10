import math
from itertools import permutations

# 소수 판별 함수
def is_prime_number(x):
    # 1 이하는 소수 아님
    if x <= 1:
        return False
    # 2부터 x의 제곱근까지의 모든 수를 확인
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    numbers_list = []
    for i in range(1, len(numbers)+1):
        numbers_list += list(permutations(numbers, i))
    # print(numbers_list)
    int_numbers_list = []
    for number_tuple in numbers_list:
        int_num = int(''.join(number_tuple))
        print(int_num)
        if int_num not in int_numbers_list:
            int_numbers_list.append(int_num)
            if is_prime_number(int_num):
                answer += 1

    return answer