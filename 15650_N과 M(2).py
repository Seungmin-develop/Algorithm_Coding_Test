import sys
from itertools import combinations
input = sys.stdin.readline

# N과 M을 입력받음
N, M = map(int, input().split())

# C에 조합의 내용들을 저장함
C = combinations(range(1, N+1), M)
# C를 돌면서 조합 내용을 출력, 이 때 i는 정수형이므로 map함수를 통해 str을 취해준 뒤 join 적용
for i in C:
    print(' '.join(map(str,i)))