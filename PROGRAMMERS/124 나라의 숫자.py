def solution(n):
    answer = ''
    while n:
        # n이 3으로 나누어지지 않으면 -> 나머지는 1 아니면 2가 나올 것이므로
        if n % 3:
            # answer 변수에 나머지를 더하고
            answer += str(n % 3)
            # 3을 나눈다
            n //= 3
        # n이 3으로 나누어지면
        else:
            # answer 변수에 4를 더하고
            answer += "4"
            # 0이 없기 때문에 n을 3으로 나누고 1을 뺀다
            n = n //3 - 1

    return answer[::-1]