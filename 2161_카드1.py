import sys
from collections import deque
from bisect import bisect_left, bisect_right
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input())
queue = deque()
count = 0
temp = 0
for i in range(1,N+1):
    queue.append(i)
    count+=1

while count>1:
    print(queue.popleft(), end=' ')
    count-=1
    temp = queue.popleft()
    queue.append(temp)

print(queue[0])