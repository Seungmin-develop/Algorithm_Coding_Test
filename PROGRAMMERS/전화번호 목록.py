def solution(phone_book):
    answer = True
    # 전화번호부를 정렬 시간복잡도 nlogn
    phone_book.sort()

    # 전화번호부를 순회하면서
    for i in range(len(phone_book)-1):
        # 현재 순회중인 전화번호의 길이를 저장
        now_num_len = len(phone_book[i])
        # 현재 순회중인 전화번호가 다음 전화번호의 접두어라면
        if phone_book[i+1][0:now_num_len] == phone_book[i]:
            print(phone_book[i][0:now_num_len])
            answer = False
            break

    return answer

solution(["123","456","789"])