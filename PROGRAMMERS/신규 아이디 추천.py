def solution(new_id):
    answer = ''

    # 1단계 lower()는 모든 알파벳을 소문자로 치환
    new_id = new_id.lower()

    # 2단계
    for elem in new_id:
        # elem이 영어, 숫자, 한글로 이루어져 있으면 True를 반환하는 isalnum 함수를 사용
        if elem.isalnum() or elem in '-_.':
            answer += elem

    # 3단계 replace()를 이용하여 ..이 나타나는 경우를 .으로 교체 while문과 같이 사용하여 ....의 경우 ....->..->. 과 같이 최종 결과물을 반환
    while '..' in answer:
        answer = answer.replace('..', '.')
    
    # 4단계
    # 맨 앞에 .이 있는 경우 .을 삭제
    if len(answer)>1 and answer[0] == '.':
        answer = answer[1:]
    
    # 맨 뒤에 .이 있는 경우 .을 삭제
    if len(answer)>1 and answer[-1] == '.':
        answer = answer[:-1]

    # answer 값이 .인 경우 빈 answer로 변환
    if len(answer)==1 and answer[0]=='.':
        answer = ''

    # 5단계 answer가 비어있는 경우 a를 넣어줌
    if answer == '':
        answer = 'a'
    
    # 6단계 answer가 16글자 이상인 경우 15글자까지 자르고 자른 결과의 맨 뒤 문자가 .인 경우 .을 삭제
    if len(answer)>=16:
        answer = answer[:15]
        if answer[-1]=='.':
            answer = answer[:-1]
    
    # 7단계 answer의 길이가 2이하인 경우 마지막 문자를 이용해 answer를 연장
    while len(answer)<=2:
        answer += answer[-1]
    
    return answer