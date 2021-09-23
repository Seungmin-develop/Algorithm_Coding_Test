import sys
from collections import deque
from bisect import bisect_left, bisect_right
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def rotate_left(queue, number):
    while queue[0]!=number:
        a1 = queue.popleft()
        queue.append(a1)
        global answer
        answer+=1

def rotate_right(queue, number):
    while queue[0]!=number:
        a1 = queue.pop()
        queue.appendleft(a1)
        global answer
        answer+=1

N, M = map(int, input().split())
count_rotate_left = 0
count_rotate_right = 0
queue = deque()
answer = 0
temp_index = 0
numbers = []
for i in range(1, N+1):
    queue.append(i)

numbers = list(map(int, input().split()))
for number in numbers:
    length = len(queue)

    for i in range(length):
        if queue[i] == number:
            temp_index = i
            break
    
    if temp_index<=length//2:
        rotate_left(queue, number)
    else:
        rotate_right(queue, number)
    
    queue.popleft()
    
print(answer)