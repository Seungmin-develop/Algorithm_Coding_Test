from collections import deque

def solution(maps):
    answer = 0
    height = len(maps)
    width = len(maps[0])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    visited = [[-1 for _ in range(width)] for _ in range(height)]

    queue = deque()
    queue.append([0, 0])
    visited[0][0] = 1
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < width and 0 <= ny < height and visited[ny][nx] == -1 and maps[ny][nx] == 1:
                visited[ny][nx] = visited[y][x] + 1
                queue.append([ny, nx])
            
    answer = visited[height - 1][width - 1]
    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))