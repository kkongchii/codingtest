def solution(distance, rocks, n):
    # 이분탐색 왤케 어렵냐
    # 각 바위 사이 거리 중 제일 작은 값이 가장 커지게 하는 케이스를 구하는 문제
    # 탐색할 범위는 거리 -> 전체 징검다리를 표현하는게 아님
    # 하나씩 지워가며 n개를 지웠을 때 최소거리와 동일할때까지
    rocks.append(distance) # 마지막 길이 지점에 돌 없을 수 있음
    rocks.sort()
    left = 1 # 거리최소값은 1
    right = distance
    answer = 0
    
    while left <= right:
        mid = (left+right)//2
        point = 0
        remove = 0
        minimum = 1000000000
        for rock in rocks:
            distance_from_point = rock - point
            if distance_from_point < mid:
                remove += 1
            else:
                point = rock
                minimum = min(distance_from_point, minimum)
        
        if n >= remove:
            answer = minimum
            left = mid + 1
        else:
            right = mid - 1
                
    return answer