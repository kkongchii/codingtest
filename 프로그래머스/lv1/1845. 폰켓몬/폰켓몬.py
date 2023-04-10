def solution(nums):
    set_poketmon = set(nums)
    if len(set_poketmon) > len(nums)/2:
        answer = len(nums)/2
    else:
        answer = len(set_poketmon)
    
    return answer