count = 0


def solution():
    n = int(input())
    board = [0 for _ in range(n)]

    def n_queen(y):
        global count
        if y == n:
            count += 1
            return
        for i in range(n):
            flag = 1
            for j in range(y):
                if board[j] == i or abs(y - j) == abs(i - board[j]):
                    flag = 0
                    break
            if flag:
                board[y] = i
                n_queen(y + 1)
    n_queen(0)
    print(count)


if __name__ == "__main__":
    solution()