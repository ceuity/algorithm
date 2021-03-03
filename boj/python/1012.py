import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        w, h, k = map(int, input().split())
        grid = [[0 for _ in range(w)] for _ in range(h)]
        for _ in range(k):
            x, y = map(int, input().split())
            grid[y][x] = 1
        answer = 0
        def dfs(i, j):
            if i < 0 or i >= h or j < 0 or j >= w:
                return
            if grid[i][j] == 1:
                grid[i][j] = 0

                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i, j-1)

        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    dfs(i, j)
                    answer += 1
        print(answer)

"""
입력을 받는 즉시 처리를 해야 해서 해당 부분만 처리해주고 나머지는 다른 dfs 문제와 비슷한 방식으로 풀었다.
백준에서는 최대 재귀 깊이 제한이 걸려있어서 제한을 해제해주어야 통과할 수 있었다.
"""