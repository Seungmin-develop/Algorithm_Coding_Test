def solution(nums):
    answer = 0
    
    nums_set = set(nums)
    len_nums_set = len(nums_set)
    if len_nums_set >= len(nums)/2:
        answer = len(nums)/2
    else:
        answer = len_nums_set
    
    return answer