import sys
input = sys.stdin.readline

N = int(input())
arr = [0] + list(map(int, input().split()))
dp = [[0]*(N+1) for _ in range(N+1)]
for i in range(N, 0, -1):
    for j in range(N, 0, -1):
        if i==j:
            dp[i][j] = 1
        elif i+1==j and arr[i]==arr[j]:
            dp[i][j] = 1
        elif j>i:
            if arr[i]==arr[j] and dp[i+1][j-1]==1:
                dp[i][j] = 1

M = int(input())

for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S][E])