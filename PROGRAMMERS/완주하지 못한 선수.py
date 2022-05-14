# 이 문제는 해시를 이용해야 하는 것으로 remove메소드를 사용하면
# 효율성에 의해 통과하지 못한다. dict를 탐색하는 것은 dict 내부가 해시로
# 구현되어 있기 때문에 O(n)의 시간복잡도를 가져 통과하게 된다.
def solution(participant, completion):
    # 사람의 이름을 키, 반복되는 이름의 횟수를 값으로 저장
    d = {}
    # 참가자들을 순회하면서
    for person in participant:
        # 이름이 같은 사람이 d에 없으면 1로 추가
        if person not in d:
            d[person] = 1
        # 이름이 같은 사람이 d에 있으면 1을 증가
        else:
            d[person] += 1

    # completion에 있는 사람의 이름을 1 감소
    for person in completion:
        d[person] -= 1

    # 값이 0보다 큰 경우 완주하지 못한 경우이기 때문에 해당 이름을 출력
    for key, value in d.items():
        if value > 0:
            print(key)
            return key