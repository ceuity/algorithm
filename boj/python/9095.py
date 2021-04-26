import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    def dfs(n):
        global count
        if n == 0:
            count += 1
        elif n < 0:
            return
        else:
            dfs(n - 1)
            dfs(n - 2)
            dfs(n - 3)
    dfs(n)
    print(count)

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        count = 0
        solution()