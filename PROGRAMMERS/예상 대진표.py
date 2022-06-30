def solution(n,a,b):
    print(n, a, b)
    count = 0
    copy_n = n
    while copy_n > 1:
        copy_n = copy_n / 2
        count += 1

    if (a <= n//2 and b > n//2) or (a > n// 2 and b <= n//2) or n==2 :
        print(count)
        return count
    
    elif a <= n//2 and b <= n//2:
        return solution(n//2, a, b)
    
    elif a > n//2 and b > n//2 :
        return solution(n//2, a-n//2, b-n//2)