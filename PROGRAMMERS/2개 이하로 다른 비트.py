def solution(numbers):
    answer = []
    bin_numbers = []
    for number in numbers:
        bin_number = bin(number)
        bin_number = list(bin_number)
        bin_number.remove('b')
        for idx in range(len(bin_number)-1, -1, -1):
            if idx != 0 and bin_number[idx] == '0':
                bin_number[idx] = '1'
                if idx == len(bin_number)-1:
                    break
                if bin_number[idx+1] == '1':
                    bin_number[idx+1] = '0'
                break
            if idx == 0 and bin_number[idx] == '0':
                bin_number[idx] = '1'
                bin_number[idx+1] = '0'
                break

        bin_number = '0b'+''.join(bin_number)

        answer.append(int(bin_number, 2))

    return answer