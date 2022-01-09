import sys
input = sys.stdin.readline

# dfs를 이용해 모든 조합을 돌면서 능력치 합의 최솟값 구하기
# index는 N까지 순회하는 도중의 현재 인덱스를 뜻함, count는 team_a의 팀원 수를 뜻함
# visited[i]가 1이면 team_a의 팀원이고 visited[i]가 0이면 team_b의 팀원임
def dfs(index, count):
    global answer
    if count==N//2:
        team_a, team_b = 0, 0
        for i in range(N):
            for j in range(N):
                # 두 사람이 team_a의 팀원이면
                if visited[i] and visited[j]:
                    team_a+=arr[i][j]
                # 두 사람이 tema_b의 팀원이면
                elif not visited[i] and not visited[j]:
                    team_b+=arr[i][j]
        answer = min(answer, abs(team_a-team_b))

    # 아직 전체 인원의 절반만큼 팀이 이루어지지 않은 경우
    for i in range(index, N):
        # 만약 visited[i]가 1이면 넘어감
        if visited[i]:
            continue
        # visited[i]가 0이면 1로 바꾸고 dfs를 통해 다음 index로 넘어감
        visited[i]=1
        dfs(i+1, count+1)
        # dfs가 종료되면 이전 상태로 되돌아오고 visited[i]를 다시 0으로 백트래킹
        visited[i]=0

N = int(input())
arr=[list(map(int, input().split())) for _ in range(N)]
visited = [0 for _ in range(N)]
answer = sys.maxsize

dfs(0,0)

print(answer)