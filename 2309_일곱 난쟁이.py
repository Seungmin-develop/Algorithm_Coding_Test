import sys
input = sys.stdin.readline

arr = []
for _ in range(9):
    arr.append(int(input()))

total = sum(arr)-100
for i in range(8):
    for j in range(i+1, 9):
        if arr[i]+arr[j]==total:
            temp_i = i
            temp_j = j
            break

del arr[temp_i]
del arr[temp_j-1]
arr.sort()
for i in range(7):
    print(arr[i])