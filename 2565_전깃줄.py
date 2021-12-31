import sys
input = sys.stdin.readline

N = int(input())
arr=[]
dp = [1]*N

# 전깃줄을 입력받아 arr에 저장
for _ in range(N):
    arr.append(list(map(int, input().split())))

# arr을 오름차순으로 정렬
arr.sort(key=lambda x: x[0])

# 가장 긴 증가하는 부분 수열(LIS)을 구해서 dp에 저장
# 수열이 감소할 때 전깃줄이 교차되기 때문
for i in range(N):
    for j in range(i):
        if arr[i][1]>arr[j][1] and dp[i]<dp[j]+1:
            dp[i]=dp[j]+1

print(N-max(dp))