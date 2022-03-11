import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
# dp[i]는 동전의 합이 i인 경우의 수를 저장
dp = [0]*(k+1)
# dp[0]은 특정 종류의 동전 하나만 들어가는 경우, 즉 1이 됨
dp[0] = 1

for i in coins:
    for j in range(i, k+1):
        if i<=j:
            dp[j] += dp[j-i]

print(dp[k])