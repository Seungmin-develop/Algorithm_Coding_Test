import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
graph = [[0]*(N+1) for _ in range(N+1)]
visited = [False]*(N+1)
count = 0

for _ in range(M):
    A, B = map(int, input().split())
    graph[A][B] = B
    graph[B][A] = A

def dfs(v):
    visited[v] = True
    for i in range(1, N+1):
        if graph[v][i] != 0 and visited[i] == False:
            dfs(i)

for i in range(1, N+1):
    if visited[i] == False:
        count+=1
        dfs(i)

print(count)