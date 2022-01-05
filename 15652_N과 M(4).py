import sys
input=sys.stdin.readline

#N과 M 입력받기
N, M = map(int, input().split())
# 빈 배열 arr 생성
arr = []

def dfs():
    # arr의 길이가 M과 일치하면 배열의 값들 연결해서 출력
    if len(arr)==M:
        print(' '.join(map(str, arr)))
        return
    # 그렇지 않으면
    else:
        for i in range(1, N+1):
            # 만약 배열에 아무것도 없으면 원소 추가
            if len(arr)==0:
                arr.append(i)
            # 배열에 무언가 있는데 마지막 원소가 i보다 같거나 작으면 i 추가 그렇지 않으면 continue
            else:
                if arr[-1]<=i:
                    arr.append(i)
                else:
                    continue
            dfs()
            arr.pop()

dfs()