from collections import deque
def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n = len(maps)
    m = len(maps[0])
    visit = [[0]*m for _ in range(n)]
    visit[0][0] = 1
    dq = deque()
    dq.append((0,0))
    
    while dq:
        # 튜플이니까 x,y 따로 두고 써야함 -> 변경 불가!
        y,x = dq.popleft()
        for i in range(4):
            nextX = x+dx[i]
            nextY = y+dy[i]
            if 0<=nextX<m and 0<=nextY<n and maps[nextY][nextX] == 1:
                if visit[nextY][nextX] == 0:
                    visit[nextY][nextX] = visit[y][x]+1
                    dq.append((nextY, nextX))
    # print(visit)
    if visit[n-1][m-1]:
        return visit[n-1][m-1]
    else:
        return -1



