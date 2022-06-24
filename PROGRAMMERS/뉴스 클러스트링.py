def solution(str1, str2):
    answer = 0
    # str1와 str2의 원소들을 담을 배열 선언
    str1_set = []
    str2_set = []
    # 합집합과 교집합 배열 선언
    union_set = []
    intersect_set = []

    # 대문자로 통일
    str1 = str1.upper()
    str2 = str2.upper()

    # 2글자씩 끊어서 배열에 저장
    for i in range(len(str1)-1):
        temp_elem = str1[i:i+2]
        if 'A' <= temp_elem[0] <= 'Z' and 'A' <= temp_elem[1] <= 'Z':
            str1_set.append(temp_elem)
    
    for i in range(len(str2)-1):
        temp_elem = str2[i:i+2]
        if 'A' <= temp_elem[0] <= 'Z' and 'A' <= temp_elem[1] <= 'Z':
           str2_set.append(temp_elem)

    # 2개의 배열을 합친 하나의 배열 생성
    str1_set_plus_str2_set = set(str1_set + str2_set)

    # 2개의 배열을 합친 배열에서 공통되는 원소를 찾아 각 배열에서 몇 개씩 나타나는지 확인
    for elem in str1_set_plus_str2_set:
        str1_count = 0
        str2_count = 0

        for str1_elem in str1_set:
            if elem == str1_elem:
                str1_count += 1

        for str2_elem in str2_set:
            if elem == str2_elem:
                str2_count += 1
        
        if str1_count != 0 and str2_count != 0:
            # 더 작은 값이 나타난 만큼 교집합 배열에 공통 원소 추가
            min_count = min(str1_count, str2_count)
            for _ in range(min_count):
                intersect_set.append(elem)
            
    # 합집합은 str1과 str2를 합친 뒤 교집합을 빼면 됨
    union_set = str1_set + str2_set
    for elem in intersect_set:
        if elem in union_set:
            union_set.remove(elem)
    
    if not str1_set and not str2_set:
        answer = 1
    
    else:
        answer = len(intersect_set) / len(union_set)

    return int(answer * 65536)