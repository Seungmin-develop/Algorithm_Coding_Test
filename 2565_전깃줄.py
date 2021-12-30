import sys
input = sys.stdin.readline

N = int(input())
arr=[]
dp = [1]*N

for _ in range(N):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: x[0])

for i in range(N):
    for j in range(i):
        if arr[i][1]>arr[j][1] and dp[i]<dp[j]+1:
            dp[i]=dp[j]+1

print(N-max(dp))