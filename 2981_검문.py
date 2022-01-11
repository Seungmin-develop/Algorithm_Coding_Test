import sys
input = sys.stdin.readline

# 최대 공약수 구하기 알고리즘 (유클리드 호제법)
def gcd(x, y):
    mod = x%y
    while mod>1:
        x = y
        y = mod
        mod = x % y
    return y

# 약수 구하는 알고리즘
def divisor(x):
    div_list=[x]
    for i in range(2, int(x**(0.5)+1)):
        if x%i==0:
            div_list.append(i)
            if x//i != i:
                div_list.append(x//i)
    div_list.sort()
    return div_list

N = int(input())

arr = []
for i in range(N):
    arr.append(int(input()))
arr.sort()

# 주어진 수들의 차를 arr_diff 배열에 저장
arr_diff = []
for i in range(N-1):
    arr_diff.append(arr[i+1]-arr[i])

# answer에 최대 공약수를 구함
if len(arr_diff)==1:
    answer = arr_diff[0]
else:
    answer = arr_diff[0]
    for i in range(1, len(arr_diff)):
        answer = gcd(answer, arr_diff[i])

div = divisor(answer)
print(" ".join(map(str, div)))