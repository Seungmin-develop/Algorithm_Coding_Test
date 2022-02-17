from inspect import stack
import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
max = 10**5
graph = [0]*(max+1)
fromArr = [0]*(max+1)

# 경로를 역추적하는 함수
def path(x):
    stackArr = []
    temp = x
    for _ in range(graph[x]+1):
        stackArr.append(temp)
        temp = fromArr[temp]
        # ::-1은 역순으로 출력
    print(' '.join(map(str, stackArr[::-1])))

def bfs(N):
    queue = deque()
    queue.append(N)
    while queue:
        x = queue.popleft()
        # 만약 목표인 K에 도달하면
        if x == K:
            # 얼마만에 K에 도달했는지 출력하고
            print(graph[x])
            # 경로를 구하는 함수 호출
            path(x)
            return
        for nx in (x-1, x+1, x*2):
            if 0<=nx<=max and graph[nx]==0:
                queue.append(nx)
                graph[nx] = graph[x]+1
                # 어디서부터 왔는지 배열에 저장 nx값은 x로부터 왔음을 저장
                fromArr[nx] = x

bfs(N)