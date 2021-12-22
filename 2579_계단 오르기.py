import sys
input = sys.stdin.readline

n = int(input())
# 계단의 개수를 입력 받는다.
arr = []

# 계단에 쓰인 점수를 리스트로 입력 받는다.
for _ in range(n):
    arr.append([int(input()),0])

# n이 1이거 2인 경우는 예외처럼 하드코딩한다.
if n==1:
    print(arr[0][0])

elif n==2:
    print(arr[0][0]+arr[1][0])

# n이 3 이상인 경우
elif n>=3:
    arr[n-2][1] = arr[n-1][0] + arr[n-2][0]
    arr[n-3][0] += arr[n-1][0]

# 도착점에서 출발점으로 가는 방법, 이차원 배열을 이용해 바로 전 계단에서 온 것인지 두 번째 전 계단에서 온건지 판단
    for i in range(n-3):
        arr[n-4-i][1] = arr[n-4-i][0] + arr[n-3-i][0]
        if arr[n-2-i][1] >= arr[n-2-i][0]:
            arr[n-4-i][0] += arr[n-2-i][1]
        else:
            arr[n-4-i][0] += arr[n-2-i][0]

    print(max(arr[0][0], arr[0][1], arr[1][0], arr[1][1]))