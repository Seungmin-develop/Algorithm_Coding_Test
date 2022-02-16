import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

# 방향을 나타내는 배열
dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

# dfs 구현
def dfs(x, y, graphList, visitedList):
    # 그래프의 방문 처리
    visitedList[y][x] = True
    # 대각선까지 포함한 8방향으로의 확장
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        # 단 확장 범위는 그래프의 내부여야 함
        if 0<=nx<w and 0<=ny<h:
            # 만약 확장하려는 곳이 1이고 해당 장소가 방문하지 않은 곳이라면
            if visitedList[ny][nx] == False and graphList[ny][nx] == 1:
                # 재귀함수 실행
                dfs(nx, ny, graphList, visitedList)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = []
    visited = [[False]*w for _ in range(h)]
    count = 0

    for i in range(h):
        graph.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if visited[i][j] == False and graph[i][j] == 1:
                dfs(j, i, graph, visited)
                count+=1

    print(count)