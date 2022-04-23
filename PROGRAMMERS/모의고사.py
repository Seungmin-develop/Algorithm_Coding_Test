def solution(answers):
    answer = []

    # 각 수포자의 찍는 패턴
    s_one = [1,2,3,4,5]*2000
    s_two = [2,1,2,3,2,4,2,5]*1250
    s_three = [3,3,1,1,2,2,4,4,5,5]*1000

    # 각각의 수포자가 맞춘 문제 개수 저장
    correct_arr = [0, 0, 0]

    # 정답과 찍은 답을 비교해가며 맞춘 문제 개수 변화
    for i in range(len(answers)):
        if answers[i] == s_one[i]:
            correct_arr[0] += 1
        if answers[i] == s_two[i]:
            correct_arr[1] += 1
        if answers[i] == s_three[i]:
            correct_arr[2] += 1
    
    # 가장 많이 맞춘 개수를 max_correct에 저장
    max_correct = max(correct_arr)

    # 가장 많이 맞춘 개수와 일치하는 맞은 개수를 가진 사람을 answer 배열에 저장
    for i in range(3):
        if correct_arr[i] == max_correct:
            answer.append(i+1)

    return answer
