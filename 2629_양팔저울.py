import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
answer = list(map(int, input().split()))
dp = [[0]*15001 for _ in range(30)]
pos = []

# 왼쪽과 오른쪽의 무게 차이가 같고 현재 index가 같으면 같은 경우로 취급
# 중복되는 경우에 해당 -> dp값으로 판단 1이면 중복되는 경우
def dfs(index, left, right):
    if abs(left-right) not in pos:
        pos.append(abs(left-right))
    
    if index==N:
        return
    
    if dp[index][abs(left-right)]==0:
        # 저울의 왼쪽에 추를 추가하거나 오른쪽에 추가하거나 어느쪽에도 추가하지 않는 경우
        dfs(index+1, left+arr[index], right)
        dfs(index+1, left, right+arr[index])
        dfs(index+1, left, right)
        dp[index][abs(left-right)]=1

dfs(0, 0, 0)

for i in answer:
    if i in pos:
        print("Y", end=' ')
    else:
        print("N", end=' ')