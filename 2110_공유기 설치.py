import sys
from collections import deque
from bisect import bisect_left, bisect_right
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input())
A = [[0]*N]*N
for i in range(N):
    for j in range(N):
        A[i][j] = (i+1)*(j+1)

print(A)