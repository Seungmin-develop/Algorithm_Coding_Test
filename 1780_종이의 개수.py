import sys
input = sys.stdin.readline

N = int(input())

minus_one_card = 0
zero_card = 0
one_card = 0

def func(arr, N, start_x, start_y):
    count_minus_one = 0
    count_zero = 0
    count_one = 0
    # 색종이를 돌면서 1과 0의 개수를 카운트
    for i in range(start_x, N+start_x):
        for j in range(start_y, N+start_y):
            if arr[i][j]==-1:
                count_minus_one+=1
            if arr[i][j]==0:
                count_zero+=1
            if arr[i][j]==1:
                count_one+=1
    # 만약에 모든 영역이 0으로 이루어져 있으면
    # 하얀색 색종이이므로 하얀 종이 카운트+1
    if count_zero==N*N:
        global zero_card
        zero_card+=1
        return
    # 모든 영역이 1이면 파란 종이 카운트 +1
    elif count_one==N*N:
        global one_card
        one_card+=1
        return
    
    elif count_minus_one==N*N:
        global minus_one_card
        minus_one_card+=1
        return
    # 파란 종이와 하얀 종이가 섞인 경우 9구역으로 분할하여 함수 실행
    else:
        func(arr, N//3, start_x, start_y)
        func(arr, N//3, start_x, start_y+N//3)
        func(arr, N//3, start_x, start_y+2*(N//3))
        func(arr, N//3, start_x+N//3, start_y)
        func(arr, N//3, start_x+N//3, start_y+N//3)
        func(arr, N//3, start_x+N//3, start_y+2*(N//3))
        func(arr, N//3, start_x+2*(N//3), start_y)
        func(arr, N//3, start_x+2*(N//3), start_y+N//3)
        func(arr, N//3, start_x+2*(N//3), start_y+2*(N//3))


arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

func(arr, N, 0, 0)
print(minus_one_card)
print(zero_card)
print(one_card)