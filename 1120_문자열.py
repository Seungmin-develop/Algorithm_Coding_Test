X, Y = input().split()

answer = 50

length_X = len(X)
length_Y = len(Y)

length_diff = length_Y - length_X

for i in range(length_diff+1):
    diff_count = 0
    for j in range(length_X):
        if X[j]!=Y[j+i]:
            diff_count += 1
    
    answer = min(answer, diff_count)

print(answer)