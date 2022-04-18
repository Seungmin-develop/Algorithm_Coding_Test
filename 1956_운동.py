import sys
input = sys.stdin.readline

INF = 1e9

V, E = map(int, input().split())
graph = [[INF]*(V+1) for _ in range(V+1)]

for i in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 플로이드-와셜 알고리즘으로 모든 노드에 대한 최단 거리를 구함
# 원래는 자기 자신에서 자기 자신으로 가는 최단거리는 0으로 설정해야 하지만 사이클을 구해야 하므로 0으로 설정하지 않음
for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

answer = INF
# 자기 자신에서 자기 자신으로 되돌아 오는 경우가 존재하면 최단 거리가 나올 것이고 존재하지 않으면 INF값이 나올 것임
for i in range(1, V+1):
    answer = min(answer, graph[i][i])

if answer == INF:
    print(-1)
else:
    print(answer)