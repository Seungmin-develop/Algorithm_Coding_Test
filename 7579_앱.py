import sys
input = sys.stdin.readline

N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))
cost_sum = sum(cost)
answer = sys.maxsize

# dp[i][j]는 i번째 앱에서 j 코스트로 얻을 수 있는 최대 메모리 값임
dp = [[0]*(cost_sum+1) for _ in range(N+1)]

for i in range(N):
    for j in range(cost_sum):
        if cost[i] > j :
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], memory[i]+dp[i-1][j-cost[i]])
        
        if dp[i][j] >= M:
            answer = min(answer, j)

if N==1:
    print(cost[0])
elif answer == sys.maxsize:
    print(N*M)
else:
    print(answer)