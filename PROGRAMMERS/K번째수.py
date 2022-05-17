def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        arr_split = array[commands[i][0]-1:commands[i][1]]
        arr_split.sort()
        answer.append(arr_split[commands[i][2]-1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))