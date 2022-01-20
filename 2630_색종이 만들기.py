import sys
input = sys.stdin.readline

# 흰 색종이와 파란 색종이를 저장할 전역 변수 생성
white_count=0
blue_count=0

# 분할 정복에 사용할 함수 arr은 색종이 배열, N은 색종이 한 변의 길이, start_x, start_y는 4분할 했을 때 시작하는 x, y 값
def func(arr, N, start_x, start_y):
    count_zero = 0
    count_one = 0
    # 색종이를 돌면서 1과 0의 개수를 카운트
    for i in range(start_x, N+start_x):
        for j in range(start_y, N+start_y):
            if arr[i][j]==0:
                count_zero+=1
            if arr[i][j]==1:
                count_one+=1
    # 만약에 모든 영역이 0으로 이루어져 있으면
    # 하얀색 색종이이므로 하얀 종이 카운트+1
    if count_zero==N*N:
        global white_count
        white_count+=1
        return
    # 모든 영역이 1이면 파란 종이 카운트 +1
    elif count_one==N*N:
        global blue_count
        blue_count+=1
        return
    # 파란 종이와 하얀 종이가 섞인 경우 4구역으로 분할하여 함수 실행
    else:
        func(arr, N//2, start_x, start_y)
        func(arr, N//2, start_x, start_y+N//2)
        func(arr, N//2, start_x+N//2, start_y)
        func(arr, N//2, start_x+N//2, start_y+N//2)
            
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

func(arr, N, 0, 0)

print(white_count)
print(blue_count)