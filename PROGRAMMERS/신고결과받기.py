import sys
from collections import defaultdict

input = sys.stdin.readline

def solution(id_list, report, k):
    
    answer = [0] * len(id_list)
    # 중복 제거
    report = set(report)

    # user_list_i_report는 키값으로 신고한 사람, 밸류값으로 신고 당한 사람을 저장하는 딕셔너리
    user_list_i_report = defaultdict(set)
    # user_reported는 키값으로 신고 당한 사람, 신고 당한 횟수를 저장하는 딕셔너리
    user_reported = defaultdict(int)
    # 신고처리가 접수된 사람들을 저장하는 suspended
    suspended = []

    for r in report:
        do_report, reported = r.split(' ')
        # 신고 당한 사람의 신고 당한 횟수 증가
        user_reported[reported] += 1
        # 신고한사람 : 신고당한사람 딕셔너리에 추가
        user_list_i_report[do_report].add(reported)

        # 신고 당한 횟수가 k라면 suspended 배열에 추가
        if user_reported[reported] == k:
            suspended.append(reported)
        
    for s in suspended:
        for i in range(len(id_list)):
            if s in user_list_i_report[id_list[i]]:
                answer[i] += 1

    return answer