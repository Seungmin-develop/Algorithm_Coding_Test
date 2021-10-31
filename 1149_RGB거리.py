import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N = int(input())
RGB_street = []

for i in range(N):
    RGB_street.append(list(map(int,input().strip().split())))

for i in range(1, N):
    RGB_street[i][0] = RGB_street[i][0]+min(RGB_street[i-1][1], RGB_street[i-1][2])
    RGB_street[i][1] = RGB_street[i][1]+min(RGB_street[i-1][0], RGB_street[i-1][2])
    RGB_street[i][2] = RGB_street[i][2]+min(RGB_street[i-1][0], RGB_street[i-1][1])

print(min(RGB_street[N-1]))