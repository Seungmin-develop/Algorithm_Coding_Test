import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)

# 방향을 나타내는 배열
dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = []
    visited = [[False]*w for _ in range(h)]
    count = 0

    for i in range(h):
        graph.append(list(map(int, input().split())))

    queue = deque()

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and visited[i][j] == False:
                count+=1
                queue.append([i, j])
                visited[i][j] = True
                while queue:
                    y, x = queue.pop()
                    for k in range(8):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0<=nx<w and 0<=ny<h:
                            if graph[ny][nx] == 1 and visited[ny][nx] == False:
                                visited[ny][nx] = True
                                queue.append([ny, nx])

    print(count)