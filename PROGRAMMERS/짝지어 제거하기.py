def solution(s):
    answer = 0
    s = list(s)
    # 스택을 이용해 문제를 풀기 위해 스택을 생성
    stack_arr = []
    # 문자열을 돌면서
    for elem in s:
        # 만약 스택이 비어 있으면
        if not stack_arr:
            # 원소 추가
            stack_arr.append(elem)
        # 스택이 비어있지 않으면
        else:
            # 스택의 가장 위에 있는 값과 현재 원소 값을 비교해서 같으면
            if stack_arr[-1] == elem:
                # pop 수행
                stack_arr.pop()
            # 같지 않으면 append 수행
            else:
                stack_arr.append(elem)
    
    # 스택이 비어 있으면 문자열이 모두 제거 된 것이므로 1 반환
    if len(stack_arr) == 0:
        answer = 1

    return answer

print(solution('baabaa'))