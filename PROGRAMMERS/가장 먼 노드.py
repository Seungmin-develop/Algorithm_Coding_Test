import heapq

def solution(n, edge):
    INF = 10e5
    answer = 0
    graph = [[] for _ in range(n+1)]
    # 그래프 간선의 정보를 저장
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    # 1번 노드로부터의 최단 거리를 저장하는 배열 dist_arr
    dist_arr = [INF]*(n+1)
    # 1번 노드부터 1번 노드까지의 거리는 0이므로 0을 저장
    dist_arr[1] = 0
    # 우선순위 큐를 저장하는 배열 선언
    priority_q = []
    # 최소 힙이 기본이고 첫번째 인자가 기준이므로 (거리, 노드)로 저장
    heapq.heappush(priority_q, (0, 1))
    # 우선순위 큐가 존재하는 동안
    while priority_q:
        # heappop을 하고
        dist, node = heapq.heappop(priority_q)
        # 만약 현재 저장되어 있는 최단거리가 더 작으면 아무 작업 수행 안함(작업 수행하면 무조건 더 커지기 때문)
        if dist > dist_arr[node]:
            continue
        # 연결되어 있는 노드들을 순회하면서
        for elem in graph[node]:
            # 만약 현재 저장되어 있는 최단거리보다 pop한 거리에 1을 더한 값이 더 작으면 최단거리 갱신하고 우선순위 큐에 삽입
            if dist_arr[elem] > dist + 1:
                dist_arr[elem] = dist + 1
                heapq.heappush(priority_q, (dist+1, elem))

    print(dist_arr[1:])
    max_dist = max(dist_arr[1:])
    for elem in dist_arr[1:]:
        if max_dist == elem:
            answer += 1

    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))