import sys
input = sys.stdin.readline

T = int(input())
# 모든 수 i에 대하여 i는 1+1+...+1이 존재하므로
# 1로 초기화
dp = [1]*10001

# i-2를 이루고 있는 수에다가 2를 더한 수를 dp[i]에 저장
for i in range(2, 10001):
    dp[i]+=dp[i-2]

# i-3을 이루고 있는 수에다가 3을 더한 수를 dp[i]에 저장
for i in range(3, 10001):
    dp[i]+=dp[i-3]

for _ in range(T):
    n = int(input())
    print(dp[n])