if __name__ == "__main__":
    n = int(input())
    connected = int(input())
    matrix = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(connected):
        x, y = map(int, input().split())
        matrix[x][y] = 1
        matrix[y][x] = 1
    infected = [1]
    queue = [1]
    while queue:
        curr = queue.pop(0)
        for i in range(1, n + 1):
            if matrix[curr][i] == 1 and i not in infected:
                queue.append(i)
                infected.append(i)
    print(len(infected) - 1)