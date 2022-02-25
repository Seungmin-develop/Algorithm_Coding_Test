import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split())
answer = 0

A = []
for _ in range(N):
    A.append(list(map(int, input().split())))
visited = [[False]*N for _ in range(N)]
union_idx = [[0]*N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j, idx):
    queue = deque()
    queue.append([i,j])
    union_count = 1
    union_sum = A[i][j]
    visited[i][j] = True
    union_idx[i][j] = idx
    while queue:
        y, x = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if (0<=nx<N and 0<=ny<N) and (L<=abs(A[ny][nx]-A[y][x])<=R) and (union_idx[ny][nx]!=idx) and visited[ny][nx] == False:
                visited[ny][nx] = True
                union_count += 1
                union_sum += A[ny][nx]
                union_idx[ny][nx] = idx
                queue.append([ny, nx])

    if union_count>1:
        avg = union_sum//union_count
        for a in range(N):
            for b in range(N):
                if union_idx[a][b] == idx:
                    A[a][b] = avg

while True:
    index = 0
    for i in range(N):
        for j in range(N):
            visited[i][j] = False
            union_idx[i][j] = 0

    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                index+=1
                bfs(i, j, index)

    if union_idx[N-1][N-1] == N*N:
        print(answer)
        break
    answer += 1