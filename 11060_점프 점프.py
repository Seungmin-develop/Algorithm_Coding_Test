import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
# 최솟값을 메모이제이션할 dp
dp = [0]*N
# 방문 가능 여부를 판단하는 배열 canVisit
canVisit = [False]*N
canVisit[0] = True

for i in range(N):
    # arr을 돌면서
    value = arr[i]
    for j in range(1, value+1):
        # 이전 단계를 방문할 수 있는 경우
        if i+j<N and canVisit[i] == True:
            # 만약 아직 한번도 도착한적 없는 곳이라면
            if dp[i+j] == 0:
                canVisit[i+j] = True
                dp[i+j] = dp[i] + 1
            # 새로 도착하는 방법이 더 작은 경우에만 값을 변경
            else:
                if dp[i+j] > dp[i]+1:
                    canVisit[i+j] = True
                    dp[i+j] = dp[i]+1

if canVisit[N-1]:
    print(dp[N-1])
else:
    print(-1)