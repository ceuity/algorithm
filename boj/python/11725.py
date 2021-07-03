import sys
from collections import defaultdict, deque

if __name__ == "__main__":
    N = int(input())
    graph = defaultdict(list)
    parents = [0 for _ in range(N + 1)]
    parents[1] = 1
    for _ in range(N - 1):
        start, end = map(int, sys.stdin.readline().split())
        graph[start].append(end)
        graph[end].append(start)
    q = deque([1])
    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            for node in graph[curr]:
                if not parents[node]:
                    parents[node] = curr
                    q.append(node)
    for i in parents[2:]:
        print(i)
