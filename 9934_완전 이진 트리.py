import sys
from collections import deque
from bisect import bisect_left, bisect_right
sys.setrecursionlimit(10000)
input = sys.stdin.readline

K = int(input())
list_array = list(map(int, input().split()))
tree_array = [[] for _ in range(K)]

def tree(list_array, level):
    mid = len(list_array)//2
    tree_array[level].append(list_array[mid])
    if len(list_array)==1:
        return
    else:
        tree(list_array[:mid], level+1)
        tree(list_array[mid+1:], level+1)

tree(list_array, 0)
for i in range(K):
    print(*tree_array[i])