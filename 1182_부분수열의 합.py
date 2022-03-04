import sys
input = sys.stdin.readline
count = 0

def main():
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))

    def dfs(idx, sum):
        global count
        if idx == N:
            return
        if sum + arr[idx] == S:
            count+=1

        dfs(idx+1, sum)
        dfs(idx+1, sum + arr[idx])

    dfs(0, 0)
    print(count)
    

if __name__=="__main__":
    main()