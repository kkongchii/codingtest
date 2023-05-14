# 가장 많이 겹치는 부분에 카메라 세워두기 반복?
# 코드 안짜봐도 모든 구간 체크하면 효율성 걸릴거 같은데,,
# 제일 먼저 차가 나가는 곳에 카메라 놓으면 놓치는건 없으니까 그렇게 가보자
def solution(routes):
    answer = 0
    # routes.sort(key=lambda x:x[0])
    # car_in = routes[0][0]
    routes.sort(key=lambda x:x[1]) # 나가는 지점 기준으로 정렬
    # car_out = routes[-1][1]
    routes_num = len(routes)
    check = [0]*routes_num
    
    while sum(check) != routes_num:
        pos = check.index(0)
        camera = routes[pos][1]
        for i in range(pos, routes_num):
            if routes[i][0] <= camera <= routes[i][1]:
                check[i] = 1
        answer += 1
    
    print(answer)
    
    return answer