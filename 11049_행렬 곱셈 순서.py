import sys
input = sys.stdin.readline

def solve(N):
    dp = [[0]*(N+1) for _ in range(N+1)]
    matrix = [[0,0]]
    for i in range(N):
        matrix.append(list(map(int, input().split())))
    
    for i in range(1, N):
        for j in range(1, N+1):
            if j == i+1:
                dp[i][j] = matrix[i][0] * matrix[i][1] * matrix[j][1]

    for i in range(N-1, 0, -1):
        for j in range(1, N+1):
            if dp[i][j] == 0 and j > i:
                dp[i][j] = min([dp[i][k]+dp[k+1][j]+matrix[i][0]*matrix[k][1]*matrix[j][1] for k in range(i, j)])
    
    print(dp[1][N])

N = int(input())
solve(N)