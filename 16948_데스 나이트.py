import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, -2, 2, -1, 1]
dy = [-2, -2, 0, 0, 2, 2]

def solve(r1, c1, r2, c2, N):
    queue = deque()
    queue.append([r1, c1])
    visited[r1][c1] = True
    while queue:
        y, x = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if visited[ny][nx] == False:
                    queue.append([ny, nx])
                    visited[ny][nx] = True
                    graph[ny][nx] = graph[y][x] + 1
    
    if visited[r2][c2] == False:
        print(-1)
    else:
        print(graph[r2][c2])

N = int(input())
visited = [[False]*N for _ in range(N)]
graph = [[0]*N for _ in range(N)]
r1, c1, r2, c2 = map(int, input().split())
solve(r1, c1, r2, c2, N)