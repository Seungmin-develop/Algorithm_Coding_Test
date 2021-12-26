import sys
input = sys.stdin.readline

# dp를 이차원 배열로 설정 행은 자리수, 열은 끝자리 수를 의미
N = int(input())
dp = [[0]*10 for _ in range(101)]

# 1자리 수
for i in range(1,10):
    dp[1][i] = 1

# 2자리부터 N자리 수 까지 저장
for i in range(2,N+1):
    # 끝자리 수가 0이거나 9인 경우는 예외 처리
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]
    # 끝자리 수가 1부터 8인 경우
    for j in range(1,9):
        dp[i][j] = (dp[i-1][j-1]+dp[i-1][j+1])%1000000000

sum = 0

for i in range(10):
    sum+=dp[N][i]

if sum>=1000000000:
    sum%=1000000000

print(sum)