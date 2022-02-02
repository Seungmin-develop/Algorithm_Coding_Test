import sys
input = sys.stdin.readline

N, B = map(int, input().split())

A = []
for i in range(N):
    A.append(list(map(int, input().split())))

# 행렬의 곱셈
def multiply(A, B, N):
    result = []
    for i in range(N):
        temp = []
        for k in range(N):
            temp_result = 0
            for j in range(N):
                temp_result += (A[i][j] * B[j][k])
            temp.append(temp_result % 1000)
        result.append(temp)
    return result

# 분할 정복을 이용한 거듭제곱, 지수의 절반을 이용하는 방법
def func(A, B):
    if B==1:
        for i in range(N):
            for j in range(N):
                A[i][j]=A[i][j]%1000
        return A
    temp = func(A, B//2)
    if B%2==0:
        return multiply(temp, temp, N)
    if B%2==1:
        return multiply(multiply(temp, temp, N), A, N)

answer = func(A, B)
for i in range(N):
    print(" ".join(map(str, answer[i])))