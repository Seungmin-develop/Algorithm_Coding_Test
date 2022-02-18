import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
max = 10**5
graph = [0]*(max+1)
visited = [False]*(max+1)
queue = deque()

def bfs(N):
    graph[N] = 1
    visited[N] = True
    queue.append(N)
    while queue:
        x = queue.popleft()
        if x==K:
            print(graph[x]-1)
            return
        for nx in (2*x, x-1, x+1):
            if 0<=nx<=max and visited[nx] == False:
                if nx==x*2:
                    graph[nx] = graph[x]
                    visited[nx] = True
                else:
                    graph[nx] = graph[x]+1
                    visited[nx] = True
                queue.append(nx)

bfs(N)