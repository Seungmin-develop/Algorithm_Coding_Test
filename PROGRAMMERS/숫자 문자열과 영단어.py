def solution(s):
    answer = 0
    num_dict = {"zero" : "0", "one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9"}

    for num_in_english in num_dict.keys():
        if num_in_english in s:
            s = s.replace(num_in_english, num_dict[num_in_english])
    
    answer = int(s)
    return answer

print(solution("onetwothree"))