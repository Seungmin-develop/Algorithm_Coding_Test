def solution(s):
    answer = len(s)
    # i는 끊는 단위 개수
    for i in range(1, len(s)+1):
        # 끊는 개수마다의 정답을 저장하는 변수 temp_answer
        temp_answer = len(s)
        # 끊은 부분 문자열을 저장하는 배열 slice_arr
        slice_arr = []
        # i 글자만큼 문자열을 끊어서 slice_arr에 저장
        for j in range(0, len(s)-i+1, i):
            slice_arr.append(list(s[j:j+i]))
        
        # 연속해서 같은 부분 문자열이 나오는지 체크하는 변수와 몇 번 연속인지 저장하는 변수
        conti_flag = False
        conti_count = 1
        for k in range(1, len(slice_arr)):
            # 만약 처음으로 앞 뒤의 부분 문자열이 같으면
            if slice_arr[k] == slice_arr[k-1] and conti_flag == False:
                temp_answer -= (i-1)
                conti_flag = True
                conti_count += 1
            # 계속해서 부분 문자열이 같은 경우
            elif slice_arr[k] == slice_arr[k-1] and conti_flag == True:
                temp_answer -= i
                conti_count += 1
                # 만약 연속하는 횟수가 10, 100, 1000의 경우 10a, 100a, 1000a와 같이 결과가 한자리 늘어나기 때문에 예외 처리를 해주어야함
                if conti_count in (10,100,1000):
                    temp_answer += 1
            # 앞의 부분 문자열과 다른 경우
            else:
                conti_flag = False
                conti_count = 1
        
        answer = min(answer, temp_answer)
    
    return answer