import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())

# 포인터를 배열의 왼쪽 끝과 오른쪽 끝에 설정
left, right = 0, n-1
count = 0

while left < right:
    # 왼쪽 포인터의 합과 오른쪽 포인터의 합을 sum에 저장 
    sum = arr[left] + arr[right]
    # 만약 x와 일치하면 오른쪽 포인터를 한칸 앞으로 당김
    if sum == x:
        count+=1
        right-=1
    # sum이 너무 작으면 왼쪽 포인터를 한칸 뒤로 밈
    elif sum < x:
        left+=1
    # sum이 너무 커도 오른쪽 포인터를 당김 -> 배열이 정렬되어있어야 하는 이유
    else:
        right-=1

print(count)