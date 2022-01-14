import sys
input = sys.stdin.readline

# 파스칼 삼각형을 dp에 저장
dp = []
for i in range(30):
    # 비정방 배열이므로 sub_dp를 만들어 파스칼 삼각형 층별로 저장
    sub_dp = []
    for j in range(i+1):
        sub_dp.append(1)
    dp.append(sub_dp)

for i in range(30):
    for j in range(i+1):
        # 파스칼 삼각형에서 1, 2층은 전부 1이므로 그냥 넘어감
        if i==0 or i==1:
            continue
        # 파스칼 삼각형에서 왼쪽 끝과 오른쪽 끝은 1이므로 그냥 넘어감
        if j==0 or j==i:
            continue
        dp[i][j]=dp[i-1][j-1]+dp[i-1][j]


T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    print(dp[K][N])