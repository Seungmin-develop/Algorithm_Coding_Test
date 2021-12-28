import sys
input = sys.stdin.readline

# N을 입력 받아 arr에 값을 저장, 최대 증가 횟수를 dp에 저장할 dp 생성
N = int(input())
arr = list(map(int,input().split()))
dp = [0]*N

# i번째 dp를 구하기 위해서는 i보다 앞에 있는 모든 arr을 돌면서 arr[i]보다 작은 수들을 찾고
# 그 중에 dp값이 가장 큰 수에 +1을 해주면 된다.
for i in range(N):
    max_temp = 0
    # i보다 앞에 있는 arr을 도는 반복문
    for j in range(i):
        # 만약 arr값이 i보다 작고 dp의 값이 임시 최대값보다 크다면
        if arr[j]<arr[i] and dp[j]>max_temp:
            max_temp = dp[j]
    dp[i] = max_temp+1

print(max(dp))