import sys
input = sys.stdin.readline

def dfs(start, depth):
    if depth == 6:
        print(*dp)
        return
    for i in range(start, len(arr)):
        dp[depth] = arr[i]
        dfs(i+1, depth+1)
    
while True:
    dp = [0]*6
    arr = list(map(int, input().split()))
    K = arr[0]
    if K == 0:
        break
    arr = arr[1:]
    dfs(0, 0)
    print()