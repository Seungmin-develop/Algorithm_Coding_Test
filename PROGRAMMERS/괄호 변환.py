def solution(p):
    answer = ''
    if check_correct_str(p):
        return p
    
    u, v = seperate_str(p)

    if check_correct_str(u):
        answer += u
        answer += solution(v)
        return answer
        
    
    answer += '('
    answer += solution(v)
    answer += ')'
    u = u[1:-1]
    u = list(u)
    for idx, elem in enumerate(u):
        if elem == '(':
            u[idx] = ')'
        elif elem == ')':
            u[idx] = '('
    
    answer += ''.join(u)
    
    return answer

def check_correct_str(s):
    stack_arr = []
    for elem in s:
        if elem == '(':
            stack_arr.append(elem)
        elif elem == ')':
            if stack_arr and stack_arr[-1] == '(':
                stack_arr.pop()
            else:
                stack_arr.append(elem)
    if not stack_arr:
        return True
    else:
        return False

def seperate_str(s):
    left_count = 0
    right_count = 0
    u_v_flag = 0
    u = ""
    v = ""
    for elem in s:
        if u_v_flag == 0:
            if elem == '(':
                left_count += 1
                u += '('
            elif elem == ')':
                right_count += 1
                u += ')'
        
        if u_v_flag == 1:
            if elem == '(':
                left_count += 1
                v += '('
            elif elem == ')':
                right_count += 1
                v += ')'
        
        if left_count == right_count and left_count > 0 and right_count >0:
            u_v_flag = 1
    return u, v