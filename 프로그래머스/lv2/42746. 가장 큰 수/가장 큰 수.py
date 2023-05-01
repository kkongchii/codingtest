def solution(numbers):
    
    if sum(numbers) == 0:
        return '0'
    str_numbers = [str(num) for num in numbers]
    str_numbers.sort(key=lambda x:x*3 ,reverse=True)
    answer = ''.join(str_numbers)
    return answer
