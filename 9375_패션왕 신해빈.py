import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    # 딕셔너리를 만들어 키를 의상의 종류, 밸류를 옷의 이름으로 저장
    dic = {}
    N = int(input())
    for i in range(N):
        item, category = map(str,input().split())
        # 만약 딕셔너리에 존재하지 않는 의상의 종류이면 추가
        if category not in dic:
            dic[category] = 1
        # 기존에 존재하는 의상의 종류이면 의상의 개수 증가
        else:
            dic[category]+=1
    answer = 1
    for val in dic.values():
        answer *= (val+1)
    # 알몸인 상태를 제외해야 하므로 -1을 해줌
    print(answer-1)