answer = 0

def solution(numbers, target):
    dfs(numbers, 0, 0, target)
    return answer

# num_arr는 주어지는 numbers배열, idx는 현재 numbers의 배열 인덱스, res는 현재까지의 계산값
# target은 목표값
def dfs(num_arr, idx, res, target):
    # 만약에 num_arr을 다 순회하고 결과값이 목표값과 같다면 답을 1추가
    if idx == len(num_arr):
        if res == target:
            global answer
            answer += 1
        return
    # 빼기 연산의 경우
    dfs(num_arr, idx+1, res-num_arr[idx], target)
    # 더하기 연산의 경우
    dfs(num_arr, idx+1, res+num_arr[idx], target)