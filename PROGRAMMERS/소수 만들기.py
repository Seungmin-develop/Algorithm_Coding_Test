import math

# 에라토스테네스의 체를 이용한 소수 구하기
def isPrimeNum(num):
    sqrt = math.sqrt(num)
    if sqrt < 2:
        return False

    for i in range(2, int(sqrt)+1):
        if num % i == 0:
            return False
    return True    
    
def solution(nums):
    answer = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if isPrimeNum(nums[i]+nums[j]+nums[k]):
                    answer += 1

    return answer