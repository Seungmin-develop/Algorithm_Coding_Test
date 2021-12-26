import sys
input = sys.stdin.readline

# N을 입력 받아 N개의 수를 arr에 저장하고 arr[i]의 최댓값은 dp[i]에 저장
N = int(input())
arr = [0]
dp = [0]*(N+1)

for _ in range(N):
    arr.append(int(input()))

# N이 1, 2, 3인 경우는 예외 처리하듯 하드 코딩
dp[1] = arr[1]

if N>=2:
    dp[2] = arr[1]+arr[2]

if N>=3:
    dp[3] = arr[3]+max(dp[0]+arr[2], dp[1])

# N이 4이상인 경우에는 바로 직전의 포도주를 선택하는 경우, 두 번째 이전 포도주를 선택하는 경우
# 세 번째 이전 포도주를 선택하는 경우로 나누어서 생각(N = 6이고 10 10 1 1 10 10이 주어지는 경우)
# 세 번째까지만 고려해야 하는 이유는 연속으로 2잔까지는 마실 수 있기 때문
if N>=4:
    for i in range(3, N+1):
        dp[i] = arr[i]+max(dp[i-3]+arr[i-1], dp[i-2], dp[i-4]+arr[i-1])

print(max(dp))