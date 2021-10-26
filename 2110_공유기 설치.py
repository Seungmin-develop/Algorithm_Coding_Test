import sys
from collections import deque
from bisect import bisect_left, bisect_right
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def binary_search(start, end):
    while start<=end:
        count = 1
        mid = (start+end)//2
        current = houses[0]
        for house in houses:
            if house >= current+mid:
                count+=1
                current = house
        if count>=C:
            start = mid+1
            global answer
            answer = mid
        else:
            end = mid-1


N, C = map(int, input().split())
houses = []
answer = 0

for _ in range(N):
    houses.append(int(input()))

houses.sort()
start = 1
end = houses[-1]-houses[0]

binary_search(start, end)
print(answer)