# 처음 든 생각은 이미 만났던 노드 도착하면 그게 방 아닌가?
# 였는데 좀 더 생각해보니 해당 노드에 왔다 갔다 식으로 도착하면 그건 방이 아님
# 그럼 만났던 노드 + 들어오는 방향 다르면 방인가? 확신은 안들지만 일단 ㄱㄱ
from collections import defaultdict
def solution(arrows):
    move = [(-1,0),(-1, 1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    visit = defaultdict(int)
    visit_direct = defaultdict(int)
    answer = 0
    now = (0,0)
    visit[(0,0)] = 1
    for arrow in arrows:
        for _ in range(2):
            nx, ny = now[0]+move[arrow][0], now[1]+move[arrow][1]
            if visit[(nx,ny)] == 0:
                visit[(nx,ny)] = 1
            elif visit_direct[(now, (nx,ny))] == 0:
                answer += 1
            visit_direct[(now, (nx,ny))] = 1
            visit_direct[((nx,ny), now)] = 1
            now = (nx, ny)
            
    # print(visit, visit_direct)
    return answer

# 테케는 통과하는데 제출하니까 다 틀린다 ㅋㅋㅋ
# 도저히 모르겠어서 검색해봤더니 특수한 경우가 있더라
# 선이 한 칸 이내에서 교차하면 길이 1짜리 사각형 내에서도 방이 4개가 나온다.
# 해결책은 이동을 2칸씩 하면 해결된다.