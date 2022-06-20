from collections import Counter
from itertools import combinations

def solution(orders, course):
    # 정답을 담는 배열
    answer = []
    # 코스의 개수를 순회하면서
    for c in course:
        # 임시적으로 생성한 코스들을 담는 배열
        temp = []
        # 주문들을 순회하면서
        for order in orders:
            # combination으로 주문의 조합을 만듦
            for li in combinations(order, c):
                res = ''.join(sorted(li))
                temp.append(res)
    
        # Counter 라이브러리를 이용해 temp배열 안에서 나타난 원소의 개수를 count
        sorted_candidates = Counter(temp).most_common()
        answer += [menu for menu, cnt in sorted_candidates if cnt > 1 and cnt == sorted_candidates[0][1]]
    return sorted(answer)

solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])