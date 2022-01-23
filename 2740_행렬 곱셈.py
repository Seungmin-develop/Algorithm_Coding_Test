from ntpath import join
import sys
input = sys.stdin.readline

A = []
B = []
result = []

# 행렬 A 정보 입력받음
N, M = map(int, input().split())
for i in range(N):
    A.append(list(map(int, input().split())))

# 행렬 B 정보 입력받음
M, K = map(int, input().split())
for i in range(M):
    B.append(list(map(int, input().split())))

# 행렬의 곱셈 구현
for i in range(N):
    temp = []
    for k in range(K):
        temp_result = 0
        for j in range(M):
            temp_result += (A[i][j] * B[j][k])
        temp.append(temp_result)
    result.append(temp)

for i in range(N):
    print(' '.join(map(str, result[i])))