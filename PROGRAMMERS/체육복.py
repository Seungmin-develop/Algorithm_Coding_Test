def solution(n, lost, reserve):
    answer = 0
    # 처음에는 모든 학생이 1벌씩 체육복이 있다고 가정
    student = [1]*(n+1)
    # 여벌을 가지고 있는 경우 1벌씩 추가해줌
    for idx in reserve:
        student[idx] += 1
    # 체육복을 잃어버린 경우 1벌씩 빼줌
    for idx in lost:
        student[idx] -= 1
    # 학생들을 순회하면서
    for i in range(1, n):
        # 체육복이 한 벌도 없으면
        if student[i] == 0:
            # 앞의 학생에게 2벌 있는지 확인 후
            if student[i-1] == 2:
                # 1벌을 빌림
                student[i-1] -= 1
                student[i] += 1
            # 앞의 학생이 2벌이 없고 뒤의 학생이 2벌이 있는 경우
            elif student[i+1] == 2:
                # 1벌을 빌림
                student[i+1] -= 1
                student[i] += 1
    
    # 체육복이 1벌 이상인 학생들은 수업에 참여가능함
    for i in range(1, n+1):
        if student[i] >= 1:
            answer += 1
            
    return answer