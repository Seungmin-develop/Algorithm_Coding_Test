import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph =[[0]] + [[i+j for j in range(1, 7)] for i in range(1, 101)]
visited = [10000]*101
answer = sys.maxsize

for i in range(N+M):
    start, end = map(int, input().split())
    graph[start].append(end)

# now는 현재 위치하고 있는 칸을 의미하고 count는 현재 칸에 도달하기 까지의 최소값을 의미
def bfs(now, count):
    queue = deque([])
    queue.append([now, count])
    visited[now] = count
    while queue:
        now, count = queue.popleft()
        # 뱀과 사다리 모두 없는 경우
        if len(graph[now])<=6:
            for i in range(len(graph[now])):
                if graph[now][i]<=100 and visited[graph[now][i]] > count+1:
                    visited[graph[now][i]] = count+1
                    queue.append([graph[now][i], count+1])
        # 뱀 또는 사다리가 존재하는 경우
        else:
            visited[graph[now][6]] = count
            queue.append([graph[now][6], count])

bfs(1, 0)

print(visited[100])