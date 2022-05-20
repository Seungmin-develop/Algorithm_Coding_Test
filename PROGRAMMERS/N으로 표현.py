def solution(N, number):
    answer = -1
    # dp[i]는 N이 i개 사용되었을 때 나오는 수들을 저장
    dp = [[] for _ in range(9)]
    dp[1].append(N)

    # N과 number가 같으면 1을 반환
    if N == number:
        return 1
 
    for i in range(2, 9):
        # N으로만 이루어진 자연수를 추가
        dp[i].append(int(str(N)*i))
        # 총 N이 i번 사용되어야 하므로 N이 j번 사용된 경우에 N이 i-j번 사용된 경우들과 조합을 하면 됨
        for j in range(1, i):
            for x in dp[j]:
                for y in dp[i-j]:
                    dp[i].append(x + y)
                    dp[i].append(x - y)
                    dp[i].append(y - x)
                    dp[i].append(x * y)
                    if y != 0:
                        dp[i].append(x // y)
                    if x != 0:
                        dp[i].append(y // x)
            # 중복되는 수를 제거
            dp[i] = list(set(dp[i]))

        if number in dp[i]:
            answer = i
            break

    return answer