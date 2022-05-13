def solution(n, times):
    answer = 0
    # 최소 시간을 1로 설정
    min_time = 1
    # 가장 시간이 오래걸리는 심사관에게 n명이 모두 심사받는 경우
    max_time = max(times)*n
    # 이분탐색
    while min_time <= max_time:
        mid_time = (min_time + max_time)//2
        # 심사를 마친 사람의 수를 저장하는 변수
        people_num = 0
        # 심사를 마친 사람의 수를 구하는 과정
        for time in times:
            people_num += mid_time // time
            # n이 넘어가면 더 볼 필요가 없음
            if people_num >= n:
                break
        
        # 심사를 마친 사람 수가 n이상이면 시간을 더 줄여도 되기 때문에 max_time의 값을 mid_time-1로 설정
        if people_num >= n:
            answer = mid_time
            max_time = mid_time - 1
        # 심사를 마친 사람 수가 n명이 안되면 시간을 더 늘려야 하므로 min_time이 mid_time+1이 되고 다시 이분탐색을 진행
        else:
            min_time = mid_time + 1

    return answer