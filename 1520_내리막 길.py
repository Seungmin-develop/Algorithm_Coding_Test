import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1]*N for _ in range(M)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(y, x):
    # 목적지에 도달하면 경우의 수를 1추가
    if x == N-1 and y == M-1:
        return 1
    # -1인지 아닌지로 방문 여부 판단
    if dp[y][x] != -1:
        return dp[y][x]
    # 방문처리
    dp[y][x] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M:
            if graph[y][x]>graph[ny][nx]:
               dp[y][x] += dfs(ny, nx)
    return dp[y][x]

print(dfs(0,0))