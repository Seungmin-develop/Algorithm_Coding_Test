import sys
from collections import deque
from bisect import bisect_left, bisect_right
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def fibo(x):
    length = len(zero)
    if x>=length:
        for i in range(length, x+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print(zero[x], one[x])

zero = [1, 0, 1]
one = [0, 1, 1]

T = int(input())
for _ in range(T):
    N = int(input())
    fibo(N)