import sys
input = sys.stdin.readline

# 문자열 2개 입력받음
str1 = input().strip()
str2 = input().strip()

# 문자열 2개의 길이를 변수에 저장
len1 = len(str1)
len2 = len(str2)

# 문자열 길이를 이용해 2차원 배열 생성
dp = [[0]*(len2+1) for _ in range(len1+1)]

# str1 : A
# str2 : C -> LCS = 1
# str1 : A
# str2 : CA -> LCS = 1 ... CAPCAK까지 반복하고 나면 str1을 1개 늘림
# str1 : AC
# str2 : C -> LCS = 1 CA -> LCS = 1 ... str1을 1개씩 증가
# 만약 str1[i]==str[j]이면 LCS가 1 증가 그렇지 않으면 기존 LCS의 최댓값을 저장

for i in range(1, len1+1):
    for j in range(1, len2+1):
        if str1[i-1]==str2[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j], dp[i][j-1])
        
print(dp[-1][-1])