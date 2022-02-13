import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
# 그래프를 표현하는 이중 배열
graph = [[0]*(N+1) for _ in range(N+1)]
# dfs의 방문 여부를 표시하는 visited 배열
dfs_visited = [False]*(N+1)
# bfs의 방문 여부를 표시하는 visited 배열
bfs_visited = [False]*(N+1)

# 간선을 그래프 배열에 표현
for i in range(M):
    A, B = map(int, input().split())
    graph[A][B] = B
    graph[B][A] = A

# 재귀함수를 이용한 dfs
def dfs(V):
    dfs_visited[V] = True
    print(V, end=' ')
    for i in graph[V]:
        if i!=0 and dfs_visited[i] == False:
            dfs(i)

# 큐를 이용한 bfs
def bfs(V):
    # 큐를 생성해서 첫 방문 노드를 삽입
    queue = deque([V])
    bfs_visited[V] = True
    # 큐가 빌때까지 반복
    while queue:
        # 큐에서 꺼낸 뒤
        V = queue.popleft()
        print(V, end=' ')
        # 꺼낸 노드에 연결된 모든 노드들을 확인
        for i in graph[V]:
            if i!=0 and bfs_visited[i]==False:
                queue.append(i)
                bfs_visited[i] = True

dfs(V)
print()
bfs(V)