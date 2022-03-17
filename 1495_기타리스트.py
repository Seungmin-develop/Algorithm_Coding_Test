import sys
input = sys.stdin.readline

N, S, M = map(int, input().split())
volume = list(map(int, input().split()))
dp = [[False]*(M+1) for _ in range(N+1)]
flag = 0

dp[0][S] = True

for i in range(1, N+1):
    for j in range(M+1):
        if dp[i-1][j]==True:
            if 0<=j-volume[i-1]<=M:
                dp[i][j-volume[i-1]] = True
            if 0<=j+volume[i-1]<=M:
                dp[i][j+volume[i-1]] = True

for i in range(M, -1, -1):
    if dp[N][i] == True:
        print(i)
        flag = 1
        break

if flag==0:
    print(-1)