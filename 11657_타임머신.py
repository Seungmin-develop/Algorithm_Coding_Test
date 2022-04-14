import sys
input = sys.stdin.readline

INF = 1e9

# 벨만 포드 알고리즘
def bf(start):
    # 시작 노드는 최단거리가 자기 자신이므로 0으로 줌
    dists[start] = 0
    # 값을 계속해서 갱신하기 때문에 N번 순회함
    # N-1번 순회해도 되는데 N번 순회하는 이유는 음수 간선이 사이클로 존재할 경우 최단 거리를 표시할 수 없는 경우가 발생하는지 여부를 판단하기 위함
    for i in range(N):
        # 모든 간선을 순회함
        for j in range(M):
            # 간선의 정보를 저장한 배열에서 현재 노드, 연결된 노드, 값을 가져옴
            cur_node = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            # cur_node를 거쳐서 next_node로 도달했을 때의 거리값이 최단거리 배열에 기록된 거리값보다 작으면 값을 갱신해줌
            if dists[cur_node]!=INF and dists[next_node] > dists[cur_node] + cost:
                dists[next_node] = dists[cur_node] + cost
                # 이미 N-1번 순회해서 값의 갱신이 더이상 일어나지 않아야 하는데 갱신이 일어난다는 것은 음수 간선에 의한 순환이 일어난다는 것임
                if i==N-1:
                    return True
    return False

# 노드의 개수 N, 간선의 개수 M
N, M = map(int, input().split())

# 간선의 정보를 저장할 배열
edges = []

# 1번 노드로부터의 최단 거리를 저장할 배열
dists = [INF] * (N+1)

# 간선의 정보를 입력받음 각 정보는 A노드에서 B노드로 갈 때 C의 값을 가짐
for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))

isCycle = bf(1)

if isCycle == True:
    print(-1)
else:
    for i in range(2, N+1):
        if dists[i] == INF:
            print(-1)
        else:
            print(dists[i])