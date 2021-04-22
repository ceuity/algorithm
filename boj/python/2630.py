if __name__ == "__main__":
    N = int(input())
    grid = []
    white = 0
    blue = 0

    for _ in range(N):
        grid.append(list(map(int, input().split())))

    def divide(x, y, n):
        global blue, white
        color = grid[y][x]
        for i in range(y, y+n):
            for j in range(x, x+n):
                if grid[i][j] != color:
                    divide(x, y, n//2)
                    divide(x, y + n//2, n//2)
                    divide(x + n//2, y, n//2)
                    divide(x + n//2, y + n//2, n//2)
                    return

        if color == 0:
            white += 1
            return
        else:
            blue += 1
            return

    divide(0, 0, N)
    print(white)
    print(blue)