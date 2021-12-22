import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
# 비정방형 배열의 입력 받는 방법
triangle_array = [list(map(int, input().split())) for i in range(n)]

# 동적 프로그래밍 밑에서부터 위로 올라가는 바텀 업 방식 이용
for i in range(n-1):
    for j in range(n-1-i):
        if triangle_array[n-1-i][j] >= triangle_array[n-1-i][j+1]:
            triangle_array[n-2-i][j] += triangle_array[n-1-i][j]
        else:
            triangle_array[n-2-i][j] += triangle_array[n-1-i][j+1]

print(triangle_array[0][0])