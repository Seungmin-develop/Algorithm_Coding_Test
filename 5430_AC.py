from audioop import reverse
import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for i in range(T):
    opr = input().rstrip()
    N = int(input())
    # 덱에다가 입력받은 문자열 중 숫자 뽑아서 저장
    d = deque(input().rstrip()[1:-1].split(","))
    # 만약 배열의 길이가 0이면 빈 덱 생성
    if N==0:
        d = deque()
    
    reverse_count = 0
    error_flag = 0
    # R이 나올때마다 배열을 뒤집는게 아니라 reverse_count의 숫자 증가
    # D가 나오면 그동안의 reverse_count의 짝,홀을 판단하여 짝수이면 popleft, 홀수이면 pop 수행
    for j in opr:
        if j=='R':
            reverse_count+=1
        if j=='D':
            if len(d)<1:
                print("error")
                error_flag=1
                break
            else:
                if reverse_count%2==1:
                    d.pop()
                else:
                    d.popleft()
    
    # 만약 reverse_count가 홀수이면 뒤집어서 출력
    if error_flag==0:
        if reverse_count%2==1:
            d.reverse()
        print("["+",".join(map(str, d))+"]")