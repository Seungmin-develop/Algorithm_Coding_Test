def solution(m, n, board):
    answer = 0
    for i in range(len(board)):
        board[i] = list(board[i])
    while True:
        break_count = 0
        break_point = []
        for i in range(m-1):
            for j in range(n-1):
                if check_breakable(j, i, board):
                    break_count += 1
                    break_point.append([j, i])
        if break_count == 0:
            break
        for elem in break_point:
            break_block(elem[0], elem[1], board)
        reorder_block(n, m, board)
    
    for i in range(m):
        for j in range(n):
            if board[i][j] == '0':
                answer += 1
    
    return answer


def check_breakable(x, y, board):
    if board[y][x] == board[y][x+1] and board[y][x+1] == board[y+1][x] and board[y+1][x] == board[y+1][x+1] and board[y][x] != '0':
        return True
    return False

def break_block(x, y, board):
    board[y][x] = '0'
    board[y+1][x] = '0'
    board[y][x+1] = '0'
    board[y+1][x+1] = '0'

def reorder_block(width, height, board):
    while True:
        move_count = 0
        for i in range(width):
            for j in range(height-1):
                if board[j][i] != '0' and board[j+1][i] == '0':
                    board[j][i], board[j+1][i] = board[j+1][i], board[j][i]
                    move_count += 1
        if move_count == 0 :
            break