import sys
input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))
subsequence_array = [0]
flag = 0

def dfs(index, sum):
    if index == N:
        return
    sum += S[index]
    subsequence_array.append(sum)
    dfs(index+1, sum)
    dfs(index+1, sum-S[index])

dfs(0,0)

subsequence_array.sort()

for i in range(len(subsequence_array)):
    if i!=subsequence_array[i]:
        print(i)
        flag = 1
        break

if flag == 0 :
    print(len(subsequence_array))