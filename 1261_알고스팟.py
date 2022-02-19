import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().rstrip().split(' '))
graph = [list(map(int, input().rstrip())) for _ in range(N)]
# 지금까지 부순 벽의 개수를 저장하는 배열 dist
dist = [[-1]*M for _ in range(N)]
queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue.append([0, 0])
    dist[0][0] = 0
    while queue:
        y, x = queue.popleft()
        # 목적지까지 도달했다면
        if y==N-1 and x==M-1:
            print(dist[y][x])
            return
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<=M-1 and 0<=ny<=N-1:
                # 만약 한번도 방문하지 않은 곳인데
                if dist[ny][nx] == -1:
                    # 벽이 아닌 빈방이라면 방문 처리하고 0-1bfs를 통해 appendleft
                    if graph[ny][nx] == 0:
                        dist[ny][nx] = dist[y][x]
                        queue.appendleft([ny, nx])
                    # 벽이라면 방문처리를 하고 오른쪽에 append -> 우선순위를 뒤로 미룸
                    else:
                        dist[ny][nx] = dist[y][x] + 1
                        queue.append([ny, nx])
                
bfs()