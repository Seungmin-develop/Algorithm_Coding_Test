def solution(board, moves):
    answer = 0
    # 뽑은 인형을 저장하는 스택 stack_arr 선언
    stack_arr = []
    # move를 돌면서
    for num in moves:
        # 가장 위에 board부터 밑으로 내려오면서 확인
        for i in range(len(board)):
            if board[i][num-1]!=0:
                # 만약 지금 뽑으려는 인형이 최근에 뽑은 인형과 같다면
                if stack_arr and stack_arr[-1]==board[i][num-1]:
                    stack_arr.pop()
                    answer+=2
                # 같지 않다면
                else:
                    stack_arr.append(board[i][num-1])
                board[i][num-1]=0
                # 한 번의 move에 한 번 인형을 뽑았다면
                break
    return answer