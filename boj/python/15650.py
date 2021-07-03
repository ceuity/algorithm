if __name__ == "__main__":
    N, M = map(int, input().split())
    stack = []

    def dfs(start):
        if len(stack) == M:
            print(" ".join(map(str, stack)))
        for i in range(start, N + 1):
            stack.append(i)
            dfs(i + 1)
            stack.pop()

    dfs(1)
