import heapq
def solution(operations):
    heap = []
    for operation in operations:
        if operation[0] == "I":
            heapq.heappush(heap, int(operation[2:]))
        else:
            if len(heap):
                if operation[2] == "-":
                    heap.pop(0)
                else:
                    heap.pop()
    
    if heap:
        answer = [max(heap), min(heap)]
    else:
        answer = [0,0]
    return answer