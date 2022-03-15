import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dots = [list(map(str, input().rstrip())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

start_x = 0
start_y = 0
isCycle = False

def dfs(x, y, count, start_x, start_y):
    global isCycle
    # 만약 사이클이 존재하면 함수를 끝낸다.
    if isCycle == True: 
        return

    # 방문처리
    visited[y][x] = True

    # 상하좌우 검사
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 만약 범위 안에 존재하고
        if 0<=nx<M and 0<=ny<N:
            # 방문한적이 없고 같은 색깔이라면
            if visited[ny][nx] == False and dots[y][x] == dots[ny][nx]:
                # count를 늘려서 재귀호출
                dfs(nx, ny, count+1, start_x, start_y)
            # 만약 방문했었고 처음으로 되돌아 간 것이라면 사이클이 있음을 의미하므로
            elif nx == start_x and ny == start_y and count>=4:
                # 사이클이 존재함을 표시
                isCycle = True
                dfs(nx, ny, count, start_x, start_y)
    
    return

for i in range(N):
    for j in range(M):
        # 간과하고 있었던 부분, 항상 visited를 초기화해주어야 사각형 형태의 사이클을 판단할 수 있다.
        visited = [[False]*M for _ in range(N)]
        if visited[i][j] == False:
            start_x = j
            start_y = i
            dfs(j, i, 1, start_x, start_y)

if isCycle:
    print("Yes")
else:
    print("No")