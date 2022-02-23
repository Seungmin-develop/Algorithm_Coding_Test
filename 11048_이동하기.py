import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dp = []
for _ in range(N):
    dp.append(list(map(int, input().split())))

# 방향설정
dx = [1, 0]
dy = [0, 1]

for i in range(N):
    for j in range(M):
        for k in range(2):
            nx = j + dx[k]
            ny = i + dy[k]
            # 1번째 행과 1번째 열 우로 움직이는 것과 아래로 움직이는 것을 먼저 수행
            if (0<=nx<M and 0<=ny<N) and (nx==0 or ny==0) :
                dp[ny][nx] += dp[i][j]
        # 대각선은 해당 열과 행의 바로 위와 왼쪽 수의 크기 비교하여 dp에 저장
        if 0<=j+1<M and 0<=i+1<N:
            if dp[i+1][j] > dp[i][j+1]:
                dp[i+1][j+1] += dp[i+1][j]
            else:
                dp[i+1][j+1] += dp[i][j+1]

print(dp[N-1][M-1])