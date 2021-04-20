from collections import deque

if __name__ == "__main__":
    N, K = map(int, input().split())
    answer = []
    table = deque([i for i in range(1, N+1)])
    while table:
        for _ in range(K):
            table.append(table.popleft())
        answer.append(table.pop())
    print(f'<{", ".join(map(str, answer))}>')