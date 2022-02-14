import sys
input = sys.stdin.readline

N = int(input())
edges = int(input())
graph = [[0]*(N+1) for _ in range(N+1)]
visited = [False]*(N+1)
count = 0

def dfs(v):
    if visited[v] == False:
        visited[v] = True
        global count
        count += 1
    for i in range(N+1):
        if graph[v][i] != 0 and visited[i] == False:
            dfs(i)

for i in range(edges):
    A, B = map(int, input().split())
    graph[A][B] = B
    graph[B][A] = A

dfs(1)
print(count-1)