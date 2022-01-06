import sys
input = sys.stdin.readline

# 같은 줄이나 대각선 줄에 퀸이 존재하는 체크하는 함수
def check(x):
    for i in range(x):
        if board[x]==board[i]:
            return False
        elif abs(board[x]-board[i]) == x-i:
            return False
    return True

# 여기서 x는 x번째 열을 뜻함
def dfs(x):
    global result
    # 만약 x번째 열이 N과 같으면 체스판을 벗어난 것이므로 종료하고 결과값에 1을 추가
    if x==N:
        result+=1
        return
    # 그렇지 않다면
    else:
        # 0번부터 N-1번 열까지 퀸을 배치해봄
        for i in range(N):
            board[x]=i
            # 퀸을 배치해보고 조건을 만족하면 다음 줄로 넘어감
            if check(x)==True:
                dfs(x+1)

N = int(input())
# board가 1차원 배열인 이유는 board안의 인덱스는 체스판의 행을 뜻하고 board값은 인덱스 행에 퀸이 놓인 열을 뜻함
# 즉 board[2]=1이면 3번째 줄에 2번째 열에 퀸이 놓인 것임(인덱스는 0부터 시작하므로)
board = [0]*N
result = 0

dfs(0)
print(result)