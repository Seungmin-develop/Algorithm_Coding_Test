def solution(rows, columns, queries):
    answer = []
    arr = []
    count = 1

    for _ in range(rows):
        temp_arr = []
        for _ in range(columns):
            temp_arr.append(count)
            count+=1
        arr.append(temp_arr)

    for elem in queries:
        start_y = elem[0]-1
        start_x = elem[1]-1
        end_y = elem[2]-1
        end_x = elem[3]-1
        width = end_x - start_x + 1
        height = end_y - start_y + 1

        temp = arr[start_y][start_x]
        temp_min = temp
        
        for i in range(start_y, start_y+height-1):
            arr[i][start_x] = arr[i+1][start_x]
            temp_min = min(temp_min, arr[i][start_x])
        
        for i in range(start_x, start_x+width-1):
            arr[end_y][i] = arr[end_y][i+1]
            temp_min = min(temp_min, arr[end_y][i])
        
        for i in range(end_y, end_y-height+1, -1):
            arr[i][end_x] = arr[i-1][end_x]
            temp_min = min(temp_min, arr[i][end_x])
        
        for i in range(end_x, end_x-width+1, -1):
            arr[start_y][i] = arr[start_y][i-1]
            temp_min = min(temp_min, arr[start_y][i])
        
        arr[start_y][start_x+1] = temp
        answer.append(temp_min)
            
    return answer

print(solution(100, 97, [[1,1,100,97]]))