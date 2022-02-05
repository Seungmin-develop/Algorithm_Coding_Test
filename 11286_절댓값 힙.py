import sys, heapq
input = sys.stdin.readline

N = int(input())
heap = []

def func(heap, x):
    if x==0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(x), x))

for _ in range(N):
    x = int(input())
    func(heap, x)