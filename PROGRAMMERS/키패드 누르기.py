def solution(numbers, hand):
    # 키패드를 저장하는 배열
    num_arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    answer = ''
    # 왼손 엄지 손가락의 위치
    left_hand_pos = [3, 0]
    # 오른손 엄지 손가락의 위치
    right_hand_pos = [3, 2]
    # 주어진 숫자 배열을 돌면서
    for num in numbers:
        # 키패드의 위치를 i와 j로 표현
        for i in range(4):
            for j in range(3):
                if num == num_arr[i][j]:
                    # j가 0이면 왼쪽 엄지 손가락으로 눌러야 하므로
                    if j == 0:
                        answer += 'L'
                        left_hand_pos = [i, j]
                    # j가 2이면 오른쪽 엄지 손가락으로 눌러야 하므로
                    elif j == 2:
                        answer += 'R'
                        right_hand_pos = [i, j]
                    # j가 1이면 가운데에 있는 것이므로 거리와 주 사용 손가락을 고려해야 함
                    else:
                        # 왼쪽 엄지 손가락으로부터의 거리와 오른쪽 엄지 손가락으로부터의 거리
                        left_dis = abs(i-left_hand_pos[0]) + abs(j-left_hand_pos[1])
                        right_dis = abs(i-right_hand_pos[0]) + abs(j-right_hand_pos[1])
                        # 거리와 주 사용 손가락을 고려했을 때 왼손으로 누르는게 편한 경우
                        if left_dis<right_dis or (left_dis==right_dis and hand=='left'):
                            answer += 'L'
                            left_hand_pos = [i, j]
                        # 오른손으로 누르는게 편한 경우
                        elif left_dis>right_dis or (left_dis==right_dis and hand=='right'):
                            answer += 'R'
                            right_hand_pos = [i, j]
                                            
    return answer