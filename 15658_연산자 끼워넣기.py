import sys
input = sys.stdin.readline

N = int(input())
number_array = list(map(int, input().split()))
opr_array = list(map(int, input().split()))
min_answer = sys.maxsize
max_answer = sys.maxsize*(-1)

def dfs(index, result):
    if index == N-1:
        global min_answer, max_answer
        max_answer = max(max_answer, result)
        min_answer = min(min_answer, result)
        return
    if opr_array[0]>0:
        opr_array[0]-=1
        dfs(index+1, result+number_array[index+1])
        opr_array[0]+=1
    if opr_array[1]>0:
        opr_array[1]-=1
        dfs(index+1, result-number_array[index+1])
        # 다시 원상태로 복귀하는 것이 포인트..!!
        # 그래야 모든 경우의 수를 확인할 수 있다
        opr_array[1]+=1
    if opr_array[2]>0:
        opr_array[2]-=1
        dfs(index+1, result*number_array[index+1])
        opr_array[2]+=1
    if opr_array[3]>0:
        opr_array[3]-=1
        dfs(index+1, result//number_array[index+1])
        opr_array[3]+=1

dfs(0, number_array[0])

print(max_answer)
print(min_answer)