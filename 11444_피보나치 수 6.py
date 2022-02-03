import sys
input = sys.stdin.readline

# 행렬의 곱셈
def multiply(A, B):
    result = []
    for i in range(2):
        temp = []
        for k in range(2):
            temp_result = 0
            for j in range(2):
                temp_result += (A[i][j] * B[j][k])
            temp.append(temp_result % 1000000007)
        result.append(temp)
    return result

# 분할 정복을 이용한 거듭제곱, 지수의 절반을 이용하는 방법
def func(A, B):
    if B==1:
        for i in range(2):
            for j in range(2):
                A[i][j]=A[i][j]%1000000007
        return A
    temp = func(A, B//2)
    if B%2==0:
        return multiply(temp, temp)
    if B%2==1:
        return multiply(multiply(temp, temp), A)

#[Fn+1 Fn]   [1 1]^n
#[Fn Fn-1] = [1 0]
N = int(input())
A = [[1,1],[1,0]]

print(func(A, N)[1][0])