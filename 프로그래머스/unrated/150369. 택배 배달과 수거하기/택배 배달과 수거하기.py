# def solution(cap, n, deliveries, pickups):
#     answer = 0
#     deliveries.reverse() # 먼집부터, 역순정렬
#     deliveries = [0] + deliveries # 0번째 추가
#     pickups.reverse()
#     pickups = [0] + pickups
#     # print(deliveries, pickups)
#     count = max(sum(deliveries), sum(pickups)) 
#     count = (count+1) //2 # 총 왕복 횟수
#     d_flag, p_flag = 1,1
    
#     for i in range(count):
#         d_cap, p_cap = cap, cap
        
#         if d_flag > p_flag:
#             distance = n-d_flag+1
#         else:
#             distance = n-p_flag+1
#         answer += distance*2
        
#         while d_cap != 0 and d_flag<=n:
#             tmp = min(deliveries[d_flag], d_cap)
#             if d_cap <= deliveries[d_flag]: # 현재 위치 택배가 뺄거보다 많으면
#                 d_cap -= tmp # tmp는 d_cap, 0이 됨
#                 deliveries[d_flag] -= tmp
#             else: # 현재 위치 택배가 뺄거보다 적으면
#                 d_cap -= tmp # tmp는 deliveries[d_flag]
#                 deliveries[d_flag] -= tmp
#                 d_flag += 1 # 다음 집으로
#             if d_flag > n:
#                 break
        
#         while p_cap != 0 and p_flag<=n:
#             tmp = min(pickups[p_flag], p_cap)
#             if p_cap <= pickups[p_flag]:
#                 pickups[p_flag] -= tmp
#                 p_cap -= tmp
#             else:
#                 pickups[p_flag] -= tmp
#                 p_cap -= tmp
#                 p_flag += 1
#             if p_flag > n:
#                 break
#         # print(deliveries, pickups, d_flag, p_flag)
        
#     # print(answer)
#     return answer

# 1. 배달이랑 수거 중 더 멀리가는 집을 답에 더한다.
# 2. cap만큼 뒤에서부터 없앤다.
# 0인 집은 그냥 명단에서 지우자
def solution(cap, n, deliveries, pickups):
    # deliveries.reverse() # 먼집부터, 역순정렬 XXXX -> 역순정렬하면 pop이 안됨
    answer = 0
    while deliveries or pickups:
        d_cap, p_cap = cap, cap
        while deliveries and deliveries[-1] == 0:
            deliveries.pop()
        while pickups and pickups[-1] == 0:
            pickups.pop()
        answer += max(len(deliveries), len(pickups))*2
        
        while d_cap and deliveries:
            if d_cap > deliveries[-1]:
                d_cap -= deliveries[-1]
                deliveries.pop()
            else:
                deliveries[-1] -= d_cap
                d_cap = 0
        while p_cap and pickups:
            if p_cap > pickups[-1]:
                p_cap -= pickups[-1]
                pickups.pop()
            else:
                pickups[-1] -= p_cap
                p_cap = 0
    
    print(answer)
    return answer
    