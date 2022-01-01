import sys
input = sys.stdin.readline

N = int(input())

# N개의 수를 arr에 저장하고 dp[0]에 arr[0]값을 대입
arr = list(map(int, input().split()))
dp = [0]*N
dp[0] = arr[0]

# 만약 dp[i-1]이 음수이면 최댓값이 되지 못하므로 dp[i-1]이 양수인 경우만 arr[i]값에 dp[i-1]값을 더해서 최댓값을 만듬
for i in range(1, N):
    if dp[i-1]<0:
        dp[i]=arr[i]
    else:
        dp[i]=dp[i-1]+arr[i]

print(max(dp))