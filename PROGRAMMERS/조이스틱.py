def solution(name):
    answer = 0
    
    # 좌우로 이동하는 횟수는 최대 이름의 길이 - 1 이다.
    min_horizontal_move = len(name) - 1

    # enumerate를 사용하면 배열을 순회할 때 index와 value를 동시에 알 수 있다.
    for idx, spell in enumerate(name):
        answer += min(ord(spell) - ord('A'), ord('Z') - ord(spell) + 1)

        # 현재 index의 다음 index를 보고 연속되는 A의 마지막 index를 찾는다.
        next_idx = idx + 1
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1
        
        # 첫 글자부터 A의 왼쪽을 찍고 다시 돌아오는 경우와 첫글자부터 오른쪽으로 가서 A의 마지막을 찍고오는 경우 중 최솟값을 구한다.
        min_horizontal_move = min(min_horizontal_move, idx * 2 + len(name) - next_idx, 2 * (len(name) - next_idx) + idx)

    answer += min_horizontal_move
    return answer