import sys, heapq
input = sys.stdin.readline

heap = []

def opr(heap, x):
    if x==0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    elif x>0:
        heapq.heappush(heap, (-x, x))

N = int(input())
for _ in range(N):
    x = int(input())
    opr(heap, x)