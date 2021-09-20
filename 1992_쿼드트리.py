import sys
from collections import deque
from bisect import bisect_left, bisect_right
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def quad_tree(array, N, x, y):
    print("(", end='')
    for i in range(4):
        count_zero = 0
        count_one = 0
        for j in range(x, x+(N//2)):
            for k in range(y, y+(N//2)):
                if array[k][j] == 1:
                    count_one += 1
                elif array[k][j] == 0:
                    count_zero += 1
        if count_one == (N//2)*(N//2):
            print(1, end='')
        elif count_zero == (N//2)*(N//2):
            print(0, end='')
        else :
            quad_tree(array, N//2, x, y)

        if i == 0:
            x+=N//2
        elif i==1:
            x-=N//2
            y+=N//2
        elif i==2:
            x+=N//2
    print(")", end='')


N = int(input())
array = []
for _ in range(N):
    array.append(list(map(int, input().strip())))

count_zero = 0
count_one = 0
for i in range(N):
    for j in range(N):
        if array[i][j] == 0:
            count_zero += 1
        else:
            count_one +=1

if count_zero == N*N:
    print(0)
elif count_one == N*N:
    print(1)
else:
    quad_tree(array, N, 0, 0)