def solution(s):
    answer = []
    arr = []
    
    s = s[:-2].replace('{', '').replace(',', ' ').split('} ')
    for elem in s:
        arr.append(list(map(int, elem.split(' '))))
    
    arr.sort(key = lambda x : len(x))
    
    for idx, elem in enumerate(arr):
        for e in elem:
            if e not in answer:
                answer.append(e)
    
    print(answer)
    return answer