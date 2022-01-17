import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# x!안에 y가 몇개 들어있는지 체크
def countNum(x, y):
    count = 0
    while x!=0:
        x=x//y
        count+=x
    return count

if M==0:
    print(0)
# nCm은 n!/(m!*(n-m)!)이므로 지수법칙을 이용
# 2와 5가 있어야 10이 만들어지므로 2의 개수와 5의 개수 중 더 작은 값만큼 10이 만들어짐
else:       
    print(min(countNum(N, 2)-countNum(M,2)-countNum(N-M,2),countNum(N, 5)-countNum(M, 5)-countNum(N-M,5)))