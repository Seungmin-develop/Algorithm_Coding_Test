import sys
input = sys.stdin.readline

def solve():
    for i in range(3):
        C, M, Y, K = map(int, input().split())
        if i==0:
            min_array = [C, M, Y, K]
        if C < min_array[0]:
            min_array[0] = C
        if M < min_array[1]:
            min_array[1] = M
        if Y < min_array[2]:
            min_array[2] = Y
        if K < min_array[3]:
            min_array[3] = K
        
    if sum(min_array)<1000000:
        print("IMPOSSIBLE")
    else:
        total = 1000000
        answer = [0, 0, 0, 0]
        for i in range(len(min_array)):
            if total - min_array[i] >= 0:
                total -= min_array[i]
                answer[i] = min_array[i]
            elif total - min_array[i] < 0:
                answer[i] = total
                break
        print(' '.join(map(str, answer)))

N = int(input())
for i in range(1, N+1):
    print("Case #%d: " %i, end='')
    solve()