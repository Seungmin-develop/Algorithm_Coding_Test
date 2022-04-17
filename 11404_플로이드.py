import sys
input = sys.stdin.readline

INF = 1e9

n = int(input())
m = int(input())

# 그래프 배열 만들고 자기 자신은 0으로 설정
graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

# 시작 도시, 도착 도시, 버스 한 번 타는데 필요한 비용을 입력받아 graph에 저장
# 이 때 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있으므로 같은 노선일 경우 최솟값을 저장
for i in range(m):
    a, b, c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c

# 특정 노드 k를 거쳐가는 경우를 생각해서 k를 안거치는 경우의 값과 k를 거치는 경우의 값을 비교해서 갱신
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] >= INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()