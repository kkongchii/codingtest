import heapq
def solution(scoville, K):
    count = 0
    # scoville.sort()
    # while scoville[0]<K:
    #     if len(scoville) < 2:
    #         return -1
    #     new = scoville.pop(0) + (scoville.pop(0)*2)
    #     scoville.append(new)
    #     scoville.sort()
    #     count += 1
    # 정확성 테스트 모두 통과
    # 효율성테스트 걸림 -> list 크기가 백만이라 매 loop마다 sort하는게 빡센가보다
    # 왜 heap인가 했더니 힙은 원소 pop, push마다 자동으로 정렬
    # 파이썬에서 따로 힙이 있나 구글링 결과 heapq 발견
    heapq.heapify(scoville)
    while scoville[0]<K:
        if len(scoville) < 2:
            return -1
        new = heapq.heappop(scoville) + (heapq.heappop(scoville)*2)
        heapq.heappush(scoville, new)
        count += 1
    
    answer = count
    return answer