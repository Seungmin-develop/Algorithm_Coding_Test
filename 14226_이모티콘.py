import sys
from collections import deque
input = sys.stdin.readline

S = int(input())
graph = [[-1]*(S+1) for _ in range(S+1)]
queue = deque()

def bfs():
    queue.append([1, 0])
    graph[1][0] = 0
    while queue:
        s, c = queue.popleft()
        # 클립보드에 현재 화면에 있는 이모티콘을 복사
        if graph[s][s]==-1:
            graph[s][s] = graph[s][c]+1
            queue.append([s, s])
        # 클립보드에 있는 이모티콘을 화면에 붙여넣기
        if s+c<=S and graph[s+c][c]==-1:
            graph[s+c][c] = graph[s][c]+1
            queue.append([s+c, c])
        # 현재 화면에 있는 이모티콘 한 개 제거
        if s-1>0 and graph[s-1][c]==-1:
            graph[s-1][c] = graph[s][c]+1
            queue.append([s-1, c])
bfs()
temp = graph[S][1]
for i in range(1, S+1):
    temp = min(temp, graph[S][i])
print(temp)