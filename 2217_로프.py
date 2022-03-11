import sys
input = sys.stdin.readline

N = int(input())
r = [int(input()) for _ in range(N)]

r.sort(reverse = True)
temp_max = r[0]

for i in range(1, N):
    temp = (i+1)*r[i]
    temp_max = max(temp_max, temp)

print(temp_max)