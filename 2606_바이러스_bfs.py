import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
edges = int(input())
graph = [[0]*(N+1) for _ in range(N+1)]
visited = [False]*(N+1)
count = 0

def bfs(v):
    queue = deque([v])
    while queue:
        v = queue.popleft()
        for i in range(N+1):
            if graph[v][i]!=0 and visited[i]==False:
                queue.append(i)
                visited[i] = True
                global count
                count+=1

for i in range(edges):
    A, B = map(int, input().split())
    graph[A][B] = B
    graph[B][A] = A

bfs(1)
print(count-1)