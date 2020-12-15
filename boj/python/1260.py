import sys

def dfs(v, matrix, result):
    result += [v]
    for i in range(len(matrix[v])):
        if matrix[v][i] == 1 and i not in result:
            dfs(i, matrix, result)
    return result

def bfs(v, matrix):
    visited = [v]
    queue = [v]
    while queue:
        n = queue.pop(0)
        for i in range(len(matrix[n])):
            if matrix[n][i] == 1 and i not in visited:
                visited.append(i)
                queue.append(i)
    return (visited)

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m, v = map(int, input().split())
    node_matrix = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, input().split())
        node_matrix[x][y] = 1
        node_matrix[y][x] = 1
    print(*dfs(v, node_matrix, []))
    print(*bfs(v, node_matrix))