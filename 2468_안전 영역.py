import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
max_height = 0
answer = 1
graph = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(N):
    sub_graph = list(map(int, input().split()))
    max_height = max(max_height, max(sub_graph))
    graph.append(sub_graph)

def solve(height, check, visited):
    count = 0
    queue = deque()

    for i in range(N):
        for j in range(N):
            if graph[i][j]<=height:
                check[i][j] = 1

    for i in range(N):
        for j in range(N):
            if check[i][j] == 0 and visited[i][j] == False:
                count += 1
                visited[i][j] = True
                queue.append([i, j])
                while queue:
                    y, x = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0<=nx<N and 0<=ny<N and visited[ny][nx] == False and check[ny][nx] == 0:
                            visited[ny][nx] = True
                            queue.append([ny, nx])
    return count

for height in range(1, max_height):
    check = [[0]*N for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    temp = solve(height, check, visited)
    answer = max(answer, temp)

print(answer)