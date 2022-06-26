def solution(numbers):
    str_numbers = []

    # 정수 배열을 문자열 배열로 바꾸어줌
    for num in numbers:
        str_numbers.append(str(num))

    # 문자열 배열을 원하는 기준으로 정렬
    str_numbers.sort(key = lambda x: x*3,reverse=True)

    # 모두 이어 붙임
    return str(int(''.join(str_numbers)))

print(solution([3, 30, 34, 5, 9]))