import sys
input = sys.stdin.readline

N = int(input())
# 만약 dp의 크기를 N+1로 하면 dp[2]가 할당이 안되기 때문에 N+2로 설정
dp = [0]*(N+2)
dp[2] = 1

# 다이나믹 프로그래밍 상향식과 메모이제이션 이용
for i in range(3, N+1):
    # 3의 배수이면서 2의 배수이면 둘 중 더 작은 부분
    if i%3==0 and i%2==0:
        dp[i] = 1+min(dp[i-1], dp[i//3], dp[i//2])
    # 3의 배수이고 2의 배수는 아닐 때
    elif i%3==0:
        dp[i] = 1+min(dp[i-1], dp[i//3])
    # 2의 배수이고 3의 배수는 아닐 때
    elif i%2==0:
        dp[i] = 1+min(dp[i-1], dp[i//2])
    # 3의 배수도 2의 배수도 아닐 때
    else:
        dp[i]=1+dp[i-1]

print(dp[N])