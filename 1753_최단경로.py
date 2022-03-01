import sys, heapq
input = sys.stdin.readline

V, E = map(int, input().split())
S = int(input())
INF = 10000000
# 인접 노드를 저장하는 배열
graph = [[] for _ in range(V+1)]
# 최단 거리 저장하는 배열
distance = [INF]*(V+1)

for _ in range(E):
    U, E, W = map(int, input().split())
    graph[U].append((E, W))

# 다익스트라 알고리즘을 실행하는 함수
def dijsktra(start):
    distance[start] = 0
    priority_q = []
    heapq.heappush(priority_q, (0, start))
    while priority_q:
        dist, now = heapq.heappop(priority_q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(priority_q, (distance[i[0]], i[0]))

dijsktra(S)

for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])