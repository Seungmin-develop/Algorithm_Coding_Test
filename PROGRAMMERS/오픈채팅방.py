def solution(record):
    answer = []
    # uid를 키로 nickname을 value로 저장할 users 딕셔너리 선언
    users = dict()

    # record에서 하나씩 분석
    for msg in record:
        # 공백으로 각 요소가 나뉘므로 문자열을 분할함
        arr = msg.split()
        # 채팅방에 들어오는 경우와 닉네임이 변경되는 경우 딕셔너리를 업데이트해줌
        if arr[0] == 'Enter':
            users[arr[1]] = arr[2]
        if arr[0] == 'Change':
            users[arr[1]] = arr[2]
    
    # 다시 한 번 record를 돌면서
    for msg in record:
        arr = msg.split()
        # 이미 uid와 nickname은 최종 nickname으로 변경된 상태이므로 들오는 경우와 나가는 경우를 answer 배열에 저장
        if arr[0] == 'Enter':
            answer.append(users[arr[1]]+"님이 들어왔습니다.")
        if arr[0] == 'Leave':
            answer.append(users[arr[1]]+"님이 나갔습니다.")
    
    return answer