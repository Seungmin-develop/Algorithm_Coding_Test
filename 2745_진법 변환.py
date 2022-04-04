import sys
input = sys.stdin.readline

N, B = input().split()
B = int(B)

# 파이썬에서는 int(string, base) 내장함수를 지원함
# base는 디폴트 값이 10이기 때문에 평소 int()를 사용하면 10진수로 변환되는 것임
print(int(N, B))