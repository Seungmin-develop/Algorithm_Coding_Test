import sys
from collections import deque
from bisect import bisect_left, bisect_right
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split(' ')))
check_arr = []
answer = 0
temp_index = 0

for elem in array:
    if not check_arr:
        check_arr.append(elem)
        answer+=1
    else:
        if elem>check_arr[-1]:
            check_arr.append(elem)
            answer+=1
        else:
            temp_index = bisect_left(check_arr, elem)
            check_arr[temp_index]=elem

print(answer)