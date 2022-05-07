def solution(lines):
    answer = 0
    # 시작 시간과 종료 시간을 저장하는 배열
    start_time = []
    end_time = []
    # 시작 시간과 종료 시간을 구해서 각 배열에 넣음
    for t in lines:
        time = t.split(' ')
        end_time.append(get_time(time[1]))
        start_time.append(get_start_time(get_time(time[1]), time[2]))

    # 종료 시간이 오름차순으로 저장되어 있다는 것을 이용하면 트래픽 하나의 종료시간을
    # 기준으로 구간을 설정하여 다른 트래픽들을 순회하면서 다른 트래픽의 시작 시간이 구간 안에 있으면
    # count를 추가한다. (다른 트래픽의 종료시간은 현재 기준이 되는 트래픽의 종료시간보다 무조건 뒤에 있으므로)
    for i in range(len(lines)):
        count = 0
        for j in range(i, len(lines)):
            if start_time[j] < end_time[i] + 1000:
                count += 1
        print(count)
        answer = max(answer, count)
    return answer

# 시간을 정수로 변환하는 함수
def get_time(t):
    hour = int(t[:2])*3600
    min = int(t[3:5])*60
    sec = int(t[6:8])
    return (hour + min + sec) * 1000 + int(t[9:])

# 시작 시간을 구하는 함수, 시작 시간도 정수로 변환해야함
def get_start_time(end_t, time):
    time = int(float(time[:-1]) * 1000)
    return end_t - time + 1