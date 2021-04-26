import sys
from collections import defaultdict
sys.setrecursionlimit(10000)

def solution():
    N, M = map(int, input().split())
    graph = defaultdict(list)
    visited = [0] * (N + 1)
    visited[0] = 1
    count = 0
    for _ in range(M):
        u, v = map(int, sys.stdin.readline().rsplit())
        graph[u].append(v)
        graph[v].append(u)

    def bfs(n):
        if visited[n]:
            return
        else:
            visited[n] = 1
            for v in graph[n]:
                bfs(v)
            return

    for i in range(1, N+1):
        if not visited[i]:
            bfs(i)
            count += 1
    print(count)


if __name__ == "__main__":
    solution()