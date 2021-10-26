import sys
from collections import deque
from bisect import bisect_left, bisect_right
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, K = int(input()), int(input())

start = 1
end = K # B[K]는 절대 K번째 수보다 클 수 없다.
res = 0

while start<=end:
    mid = (start+end)//2
    count = 0
    for i in range(1,N+1):
        count+=min(mid//i, N)
    if count>=K:
        end = mid-1
        res = mid
    else:
        start = mid+1

print(res)