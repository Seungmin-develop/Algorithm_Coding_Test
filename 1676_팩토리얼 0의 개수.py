import sys
input = sys.stdin.readline

# N과 팩토리얼을 저장할 dp를 생성
N = int(input())
dp = []

# 1 팩토리얼은 항상 있어야 하므로 1을 dp에 추가
dp.append(1)
# dp에 팩토리얼 값 추가
for i in range(1, N):
    dp.append(dp[i-1]*(i+1))

count = 0
while True:
    # 만약 팩토리얼 값의 마지막 수가 0이면
    if dp[N-1]%10==0:
        count+=1
        dp[N-1]=dp[N-1]//10
    # 그렇지 않으면
    else:
        break

print(count)