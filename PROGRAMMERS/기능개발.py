def solution(progresses, speeds):
    # 답을 저장할 배열 answer
    answer = []
    # 남은 날짜를 저장할 배열 day_left_arr
    day_left_arr = []
    # 답을 구하기 위한 스택 stack_arr
    stack_arr = []

    for i in range(len(progresses)):
        # 남은 진행률을 구하고 일의 효율을 구해서 남은 작업 일수를 day_left_arr에 저장
        progress_left = 100 - progresses[i]
        # 만약 남은 일을 처리해야되는 작업 일수가 정수로 떨어지면 그대로 추가하면 되지만
        if progress_left % speeds[i] == 0:
            day_left = (progress_left // speeds[i])
        # 정수로 나누어 떨어지지 않으면 소수점을 올림해야 한다. 이때 math 라이브러리를 사용해도 된다.
        else:
            day_left = (progress_left // speeds[i]) + 1
        day_left_arr.append(day_left)
    
    for i in range(len(day_left_arr)):
        # 만약 스택이 비어있지 않으면
        if stack_arr:
            # 현재 보고 있는 값이 스택의 최하단 값보다 크면(앞의 작업들이 현재 작업보다 빨리 완료가 된다면)
            if day_left_arr[i] >stack_arr[0]:
                # 정답 배열에 스택의 길이를 저장하고 스택을 비운다
                answer.append(len(stack_arr))
                stack_arr.clear()
                # 비운 뒤 현재 값을 스택에 넣는다
                stack_arr.append(day_left_arr[i])
            # 현재 보고 있는 값이 스택의 최하단 값보다 작거나 같으면(즉 앞의 작업이 완료되지 않았다면)
            else:
                # 스택에 현재 보고 있는 값을 푸시
                stack_arr.append(day_left_arr[i])
        # 만약 스택이 비어있으면
        else:
            stack_arr.append(day_left_arr[i])

    if stack_arr:
        answer.append(len(stack_arr))

    return answer