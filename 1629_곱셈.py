import sys
input = sys.stdin.readline

# A, B, C를 입력받는다.
A, B, C = map(int, input().split())

def func(A, B):
    # 만약 B가 1이라면 A%C를 출력
    if B==1:
        return A%C
    else:
        # 원래 지수의 절반을 이용해 temp를 구한다.
        temp = func(A, B//2)
        # 만약 B가 짝수였다면, 2^10 = (2^5) * (2^5)이므로 temp * temp를 해준다.
        if B%2==0:
            return (temp*temp)%C
        # 만약 B가 홀수였다면, 2^11 = 2 * (2^5) * (2^5)이므로 A * temp * temp를 해준다.
        else:
            return (A*temp*temp)%C

print(func(A,B))