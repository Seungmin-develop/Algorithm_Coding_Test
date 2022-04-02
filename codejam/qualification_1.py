import sys
input = sys.stdin.readline

def solve(R, C):
    arr = []
    for i in range(2*R+1):
        sub_arr = []
        for j in range(2*C+1):
            if (i==0 and j==0) or (i==0 and j==1) or (i==1 and j==0):
                sub_arr.append('.')
            elif i%2==0:
                if j%2==0:
                    sub_arr.append('+')
                else:
                    sub_arr.append('-')
            else:
                if j%2==0:
                    sub_arr.append('|')
                else:
                    sub_arr.append('.')
        arr.append(''.join(sub_arr))
    print('\n'.join(arr))

N = int(input())
for i in range(N):
    R, C = map(int, input().split())
    print("Case #%d:" %(i+1))
    solve(R, C)