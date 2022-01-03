import sys
input = sys.stdin.readline

N, K = map(int, input().split())

weight_arr = [0]
value_arr = [0]

# 무게와 가치를 입력받아 각각의 배열에 저장
for i in range(N):
    w, v = map(int, input().split())
    weight_arr.append(w)
    value_arr.append(v)

# dp를 만들어 값들을 저장, 이 때 dp[i][j]는 첫 물건부터 i번째 물건까지 살펴보고 배낭의 용량이
# j일때 가치의 최댓값을 저장
dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1, K+1):
        # 만약 i번째 물건의 무게가 j보다 크면 배낭에 i번째 물건을 넣을 수 없기 때문에 dp는 이전 물건까지
        # 고려한 최댓값을 가져와서 대입
        if weight_arr[i]>j:
            dp[i][j]=dp[i-1][j]
        # 만약 i번째 물건을 배낭에 넣을 수 있다면, i번째 물건을 배낭에 넣었을 때와 넣지 않는 경우의 최댓값을 비교
        else:
            dp[i][j]=max(dp[i-1][j], dp[i-1][j-weight_arr[i]]+value_arr[i])

print(dp[N][K])