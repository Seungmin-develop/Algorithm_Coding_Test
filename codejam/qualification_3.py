import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    dice = list(map(int, input().split()))
    dice.sort()
    straight_count = 0
    for elem in dice:
        if straight_count < elem:
            straight_count += 1
        else:
            continue
    print(straight_count)

T = int(input())
for i in range(1, T+1):
    print("Case #%d: " %i, end='')
    solve()