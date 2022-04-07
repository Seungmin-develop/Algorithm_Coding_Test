import sys, heapq
input = sys.stdin.readline

INF = 1e9

# 다익스트라 알고리즘
def dijkstra(S):
    dist_arr = [INF]*(n+1)
    dist_arr[S] = 0
    q = []
    heapq.heappush(q, (0, S))
    while q:
        dist, now = heapq.heappop(q)
        if dist_arr[now] < dist:
            continue
        for i in graph[now]:
            if dist_arr[i[0]] > dist + i[1]:
                dist_arr[i[0]] = dist + i[1]
                heapq.heappush(q, (dist+i[1], i[0]))
    return dist_arr

T = int(input())

for _ in range(T):
    answer = []
    # 각각 교차로(정점), 도로(간선), 목적지 후보의 개수
    n, m, t = map(int, input().split())
    # s는 출발지, g, h는 지나간 정점
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    # 목적지 후보 저장하는 배열
    candidate = []
    for _ in range(t):
        candidate.append(int(input()))

    # 기준 노드가 s, g, h인 다익스트라 알고리즘을 구현
    s_d = dijkstra(s)
    g_d = dijkstra(g)
    h_d = dijkstra(h)

    for elem in candidate:
        # 만약 s->g, g->h, h->elem 이 s->elem과 같거나 s->h, h->g, g->elem 이 s->elem과 같다면 정답 배열에 추가
        if s_d[g] + g_d[h] + h_d[elem] == s_d[elem] or s_d[h] + h_d[g] + g_d[elem] == s_d[elem]:
            answer.append(elem)
    
    answer.sort()
    print(' '.join(map(str, answer)))