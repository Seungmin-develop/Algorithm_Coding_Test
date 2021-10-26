import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

dp = [[[0]*21 for _ in range(21)]for _ in range(21)]
dp[0][0][0] = 1

def W(a, b, c):
    if a<=0 or b<=0 or c<=0:
        return 1
    elif a>20 or b>20 or c>20:
        return W(20,20,20)

    if dp[a][b][c]:
        return dp[a][b][c]
    elif a<b and b<c:
        dp[a][b][c] = W(a, b, c-1) + W(a, b-1, c-1) - W(a, b-1, c)
        return dp[a][b][c]
    else:
        dp[a][b][c] = W(a-1, b, c)+W(a-1,b-1,c)+W(a-1,b,c-1)-W(a-1,b-1,c-1)
        return dp[a][b][c]

while(True):
    a, b, c = map(int, input().split())
    if a==-1 and b==-1 and c==-1:
        break
    answer = W(a, b, c)
    print("w(%d, %d, %d) = %d"%(a,b,c,answer))