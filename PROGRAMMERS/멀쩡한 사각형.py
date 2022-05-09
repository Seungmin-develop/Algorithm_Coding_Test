# 최대 공약수를 구하는 함수
def gcd(a,b):
    if a%b == 0:
        return b
    return gcd(b, a%b)

def solution(w,h):
    answer = 0
    # 최대 공약수가 있는 지점을 제외하고는 직선이 지나는 구역의 개수는 가로, 세로의 길이의 합과 같음
    answer = w*h - (w+h-gcd(w,h))
    return answer