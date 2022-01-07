import sys
input = sys.stdin.readline

# 스도쿠 판을 저장할 board와 0이 있는 위치를 저장할 zero 생성
board=[]
zero=[]

# dfs + 백트래킹
def dfs(idx):
    # 만약 zero 배열을 다 순회했다면 스도쿠 판이 완성된 것이므로 출력
    if idx == len(zero):
        for i in range(9):
            print(*board[i])
        # 여기서 return이 아니라 exit(0)를 써야 1가지 경우만 출력하고 종료
        exit(0)
    # 만약 zero 배열을 다 순회하지 않았으면
    else:
        # 1부터 9까지 넣어보면서 스도쿠 조건에 맞는지 확인
        for i in range(1,10):
            # 0의 위치를 다른 변수에 저장
            zero_x = zero[idx][0]
            zero_y = zero[idx][1]

            # 만약 board[zero_x][zero_y]에 어떤 수 i를 넣어도 스도쿠 조건에 어긋나지 않으면
            # i를 board에 넣고 다음 0이 존재하는 곳에서 dfs 재귀실행
            if check(zero_x, zero_y, i):
                board[zero_x][zero_y]=i
                dfs(idx+1)
                # 만약 다음 dfs를 갔는데 규칙에 어긋나는 경우 밖에 없게되면 다시 돌아와서 board[zero_x][zero_y]값을 0으로 바꾸고
                # 다른 i 값을 대입해봐야함
                board[zero_x][zero_y]=0

# 스도쿠 조건에 위배되는지 체크하는 함수
def check(x, y, i):
    # 가로와 세로 체크
    for j in range(9):
        if board[x][j]==i:
            return False
        if board[j][y]==i:
            return False
    
    # 3*3 구역 체크
    nx=x//3*3
    ny=y//3*3

    for j in range(3):
        for k in range(3):
            if board[nx+j][ny+k]==i:
                return False
    
    return True


for _ in range(9):
    board.append(list(map(int, input().split())))

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            zero.append([i,j])

dfs(0)