import sys
input = sys.stdin.readline

# N과 M을 입력받음
N, M = map(int, input().split())

arr=[]

def dfs():
    # 만약 arr의 길이가 M과 같아지면 arr을 한줄로 출력
    if len(arr)==M:
        print(' '.join(map(str, arr)))
        return
    # 만약 arr의 길이가 M과 같지 않으면 arr에 i를 추가하고 dfs 수행
    # dfs가 종료되면, 즉 arr의 길이가 M이 되어 멈추고 나면 pop을 수행
    # pop을 수행함으로써 다음에 출력해야할 숫자로 넘어감(dfs)
    else:
        for i in range(1, N+1):
            arr.append(i)
            dfs()
            arr.pop()

dfs()