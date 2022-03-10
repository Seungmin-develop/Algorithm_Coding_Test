import sys, math
input = sys.stdin.readline

N = int(input())
max = math.ceil(100000**(1/2))
dp = [0]*100001

for i in range(1, max):
    dp[i*i] = 1

for i in range(2, N+1):
    if dp[i] == 1:
        continue
    else:
        dp[i] = min(dp[j*j]+dp[i-j*j] for j in range(1, math.ceil(i**(1/2))))

print(dp[N])