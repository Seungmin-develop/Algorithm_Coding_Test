from collections import deque

def solution(places):
    answer = []
    for elem in places:
        is_distance = True
        for i in range(len(elem)):
            for j in range(len(elem[i])):
                
                if elem[i][j] == 'P':
                    visited = [[False]*5 for _ in range(5)]
                    dist = [[0]*5 for _ in range(5)]
                    bfs(j, i, visited, dist, elem)
                    
                    for k in range(5):
                        for l in range(5):
                            if (dist[k][l] == 1 or dist[k][l] == 2) and elem[k][l] == 'P':
                                is_distance = False
        
        if is_distance:
            answer.append(1)
        else:
            answer.append(0)
    
    return answer

def bfs(start_x, start_y, visited, dist, place):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    queue.append([start_y, start_x])
    visited[start_y][start_x] = True
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<5 and 0<=nx<5 and (place[ny][nx] == 'O' or place[ny][nx] == 'P') and visited[ny][nx] == False:
                visited[ny][nx] = True
                dist[ny][nx] = dist[y][x] + 1
                queue.append([ny, nx])