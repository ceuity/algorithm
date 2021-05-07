from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def solution(board):
    def bfs(start):
        n = len(board)
        dp = [[float('inf') for _ in range(n)] for _ in range(n)]
        dp[0][0] = 0
        q = deque([start])
        while q:
            y, x, cost, dir = q.popleft()
            for i in range(4):
                xi = x + dx[i]
                yi = y + dy[i]
                if i != dir:
                    next_cost = cost + 600
                else:
                    next_cost = cost + 100
                if 0 <= xi < n and 0 <= yi < n and board[yi][xi] == 0 and dp[yi][xi] > next_cost:
                    dp[yi][xi] = next_cost
                    q.append([yi, xi, next_cost, i])
        return dp[-1][-1]

    return min(bfs([0, 0, 0, 0]), bfs([0, 0, 0, 2]))


if __name__ == "__main__":
    board = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]
    print(solution(board))