def solution(N, stages):
    answer = []
    total_people_num = len(stages)
    stages.sort()
    clear_dict = {}
    fail_dict = {}
    
    for i in range(1, N+1):
        fail_dict[i] = 0.0
    
    for elem in stages:
        if elem in clear_dict:
            clear_dict[elem] += 1
        else:
            clear_dict[elem] = 1
    
    now_elem = -1
    for idx, elem in enumerate(stages):
        if elem == N+1:
            continue
        else:
            if elem != now_elem:
                now_elem = elem
                fail_dict[elem] = clear_dict[elem]/(total_people_num - idx)
            
    sorted_fail_dict = sorted(fail_dict.items(), reverse = True, key = lambda x : x[1])
    for elem in sorted_fail_dict:
        answer.append(elem[0])
    
    return answer