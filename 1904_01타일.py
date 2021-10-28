import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
dp = [0]*1000001
dp[1] = 1
dp[2] = 2

def func(N):
    for i in range(3,N+1):
        dp[i]=(dp[i-2]+dp[i-1])%15746

N = int(input())
func(N)
print(dp[N])