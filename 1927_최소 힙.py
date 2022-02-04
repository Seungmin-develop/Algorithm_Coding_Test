import sys, heapq
input = sys.stdin.readline

N = int(input())
heap = []

def opr(heap, x):
    if x==0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    elif x>0:
        heapq.heappush(heap, x)

for _ in range(N):
    x = int(input())
    opr(heap, x)
