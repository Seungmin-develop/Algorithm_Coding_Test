import sys, heapq
input = sys.stdin.readline

INF = 1e9

def dijkstra(S, E):
    # S정점으로부터 각 정점의 최단 거리를 저장하는 배열 dis_arr
    dis_arr = [INF]*(N+1)
    # 우선순위 큐
    q = []
    heapq.heappush(q, (0, S))
    dis_arr[S] = 0
    while q:
        # dis는 now 정점까지의 최단 거리, now는 현재 정점
        dis, now = heapq.heappop(q)
        # 이미 저장되어 있는 값이 dis보다 작으면 방문했다고 여기고 큐에서 다음 값을 꺼냄
        if dis_arr[now] < dis:
            continue
        # 연결 정점에 연결되어 있는 정점들을 돌면서
        for i in graph[now]:
            # now 정점을 거쳐서 가면 더 값이 작은 경우
            if dis_arr[i[0]] > dis + i[1]:
                dis_arr[i[0]] = dis + i[1]
                heapq.heappush(q, (dis + i[1], i[0]))
    return dis_arr[E]

N, E = map(int, input().split())

# 그래프 정보 저장하는 배열
graph = [[] for _ in range(N+1)]

for i in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

# v1, v2를 반드시 거쳐야 하므로 경로는 두 가지가 나온다.
path1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
path2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

if path1 >= 1e9 and path2 >= 1e9:
    print(-1)
else:
    print(min(path1, path2))