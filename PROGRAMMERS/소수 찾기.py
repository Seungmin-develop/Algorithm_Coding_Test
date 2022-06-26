from itertools import permutations
from math import sqrt

def solution(numbers):
    answer = 0
    # 문자열 배열을 정수로 변환
    int_numbers = []
    # 중복되는 수 중복 방지를 위한 배열
    flag_arr = []
    # 문자열 배열을 정수 배열로 변환
    for num in numbers:
        int_numbers.append(int(num))

    # 정수 배열의 길이를 저장
    numbers_len = len(int_numbers)
    for i in range(1, numbers_len + 1):
        for j in permutations(int_numbers, i):
            # 정수 배열을 순열을 통해 돌면서 소수인지 확인할 숫자를 저장
            check_num = int(''.join(map(str, j)))

            # 만약 확인할 숫자가 2 이상이고 소수이며 중복되지 않은 수이면
            if check_num >= 2 and isPrimeNum(check_num) and check_num not in flag_arr:
                flag_arr.append(check_num)
                answer += 1

    return answer

# 소수인지 판별하는 함수
def isPrimeNum(num):
    s = int(sqrt(num))
    # 확인하고자 하는 숫자의 제곱근까지만 약수가 있는지 확인 (에라토스테네스의 체)
    for i in range(2, s+1):
        if num % i == 0 :
            return False
    return True