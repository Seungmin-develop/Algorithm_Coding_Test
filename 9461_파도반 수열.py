import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def func(num, array):
    if array[num]!=0:
        return array[num]
    else:
        array[num]=func(num-1, array)+func(num-5, array)
        return array[num]

dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
dp_after = [0]*90
dp.extend(dp_after)

T = int(input())
for _ in range(T):
    N = int(input())
    print(func(N, dp))