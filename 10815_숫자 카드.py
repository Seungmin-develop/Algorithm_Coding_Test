import sys
input = sys.stdin.readline

N = int(input())
N_array = list(map(int, input().split()))
M = int(input())
M_array = list(map(int, input().split()))
isHave = [0]*M

N_array.sort()

def binary_search(i, start, end):
    if N_array[start] == M_array[i] or N_array[end] == M_array[i]:
        isHave[i] = 1
        return True
    if start>=end:
        return False
    mid = (start+end)//2
    if M_array[i] > N_array[mid]:
        binary_search(i, mid+1, end)
    else:
        binary_search(i, start, mid)

for i in range(M):
    binary_search(i, 0, N-1)

print(" ".join(map(str, isHave)))