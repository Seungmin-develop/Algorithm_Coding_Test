from collections import deque

def solution(priorities, location):
    answer = 0
    # 인쇄 목록을 queue로 만들어 넣음
    queue = deque()

    # index와 value를 동시에 넣어서 location과 index를 비교할 수 있도록 함
    for idx, priority in enumerate(priorities):
        queue.append([idx, priority])
    
    # priorities가 존재할 때까지
    while priorities:
        # 만약 우선순위가 가장 높은 문서가 queue의 가장 앞에 있으면
        if queue[0][1] == max(priorities):
            answer += 1
            priorities.remove(queue[0][1])
            # 해당 문서가 location과 같다면
            if queue[0][0] == location:
                break
            queue.popleft()
        # 그 외의 경우
        else:
            temp = queue.popleft()
            queue.append(temp)
    
    return answer