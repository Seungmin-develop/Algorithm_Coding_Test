from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque()
    for idx, priority in enumerate(priorities):
        queue.append([idx, priority])
    
    while priorities:
        if queue[0][1] == max(priorities):
            answer += 1
            priorities.remove(queue[0][1])
            if queue[0][0] == location:
                break
            queue.popleft()
        else:
            temp = queue.popleft()
            queue.append(temp)
    
    return answer

print(solution([1, 1, 9, 1, 1, 1], 0))