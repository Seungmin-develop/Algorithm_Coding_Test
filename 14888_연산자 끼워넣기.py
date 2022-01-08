import sys
from itertools import permutations
input = sys.stdin.readline

# 피연산자 2개와 연산자가 주어졌을 때 계산하는 함수
def cal(x, y, opr):
    if opr == 0:
        return x+y
    elif opr == 1:
        return x-y
    elif opr == 2:
        return x*y
    elif opr == 3:
        if x<0 and y>0:
            x *= -1
            return -1*(x//y)
        return x//y

# N을 입력받고 N개의 수를 number 리스트에 저장
N = int(input())
number = list(map(int, input().split()))
# 연산자의 개수를 입력받아 operator_count 리스트에 저장
operator_count = list(map(int, input().split()))
# operator_count의 인덱스를 이용해 operator_arr에 연산자들을 저장해서 나열
operator_arr = []
for i in range(4):
    while operator_count[i]!=0:
        operator_arr.append(i)
        operator_count[i]-=1

result = []

# 나열한 연산자들을 순열로 돌면서 계산한 뒤 result 배열에 저장하고 그중에서 max, min을 찾아 출력
for i in permutations(operator_arr, N-1):
    temp = cal(number[0], number[1], i[0])
    for j in range(2, N):
        temp = cal(temp, number[j], i[j-1])
    result.append(temp)

print(max(result))
print(min(result))