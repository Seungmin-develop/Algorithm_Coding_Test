import sys
input = sys.stdin.readline

# N 입력받고 arr 배열에 저장
N = int(input())
arr = list(map(int, input().split()))

# dp[i]에는 arr[i]를 극댓값으로 가지는 바이토닉 수열의 길이의 최댓값을 저장
# dp_increase[i]에는 왼쪽에서부터 증가하는 수열의 최댓값을 저장
# dp_decrease[i]에는 오른쪽에서부터 증가하는 수열의 최댓값을 저장 -> 결국에는 감소하는 수열이 됨
# 따라서 dp_increase[i]와 dp_decrease[i]의 합을 통해 바이토닉 수열의 길이의 최댓값을 구할 수 있음
dp = [1]*N
dp_increase = [1]*N
dp_decrease = [1]*N

# dp_increase값 찾기
for i in range(1, N):
    max_temp = 0
    for j in range(i):
        if arr[j]<arr[i] and max_temp<dp_increase[j]:
            max_temp = dp_increase[j]
    dp_increase[i]=max_temp+1

# dp_decrease값 찾기
for i in range(1, N):
    max_temp = 0
    for j in range(i):
        if arr[N-1-j]<arr[N-1-i] and max_temp<dp_decrease[N-1-j]:
            max_temp = dp_decrease[N-1-j]
    dp_decrease[N-1-i]=max_temp+1

# dp값 찾기
for i in range(N):
    dp[i] = dp_increase[i]+dp_decrease[i]

print(max(dp)-1)